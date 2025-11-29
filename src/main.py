from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

from src.agents.backend.quiz_agent import QuizAgent
from src.agents.backend.explanation_agent import ExplanationAgent
from src.agents.backend.scheduler_agent import SchedulerAgent
from src.services.session_service import InMemorySessionService
from src.memory.memory_bank import MemoryBank

app = FastAPI(title="Personalized Learning Assistant")

# CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = InMemorySessionService()
mem = MemoryBank()
_bg_tasks = {}

async def generate_learning_bundle(ctx: Dict[str, Any]) -> Dict[str, Any]:
    """Parallel agents: Quiz + Explanation run concurrently."""
    q = QuizAgent()
    e = ExplanationAgent()
    results = await asyncio.gather(q.run(ctx), e.run(ctx))
    bundle = {}
    for r in results:
        bundle.update(r)
    return bundle

@app.get("/")
def root():
    return {"message": "Personalized Learning Assistant API", "status": "running"}

@app.post("/quiz")
async def quiz_agent(payload: Dict[str, Any]):
    ctx = {"topic": payload.get("topic", "general")}
    agent = QuizAgent()
    result = await agent.run(ctx)
    mem.add(payload.get("user_id", "anon"), {"type": "quiz", "content": result})
    return result

@app.post("/explain")
async def explain_agent(payload: Dict[str, Any]):
    ctx = {"concept": payload.get("concept", payload.get("topic", "concept"))}
    agent = ExplanationAgent()
    result = await agent.run(ctx)
    mem.add(payload.get("user_id", "anon"), {"type": "explanation", "content": result})
    return result

@app.post("/start_session")
async def start_session(payload: Dict[str, Any], background_tasks: BackgroundTasks):
    user = payload.get("user_id", "user1")
    sid = sessions.create(user, payload)
    logger.info("Created session %s", sid)
    task = asyncio.create_task(_scheduler_loop(sid, payload))
    _bg_tasks[sid] = task
    return {"session_id": sid, "status": "active"}

@app.post("/pause_session")
def pause_session(payload: Dict[str, Any]):
    sid = payload["session_id"]
    sessions.pause(sid)
    return {"status": "paused", "session_id": sid}

@app.post("/resume_session")
def resume_session(payload: Dict[str, Any]):
    sid = payload["session_id"]
    sessions.resume(sid)
    return {"status": "resumed", "session_id": sid}

@app.post("/generate_bundle")
async def generate(payload: Dict[str, Any]):
    ctx = {
        "topic": payload.get("topic"),
        "concept": payload.get("concept"),
        "user_id": payload.get("user_id", "anon")
    }
    bundle = await generate_learning_bundle(ctx)
    mem.add(ctx["user_id"], {"type": "bundle", "content": bundle})
    logger.info("Generated bundle for %s", ctx["user_id"])
    return bundle

@app.get("/memory/{user_id}")
def get_user_memory(user_id: str):
    return {"user_id": user_id, "memory": mem.query_recent(user_id, limit=10)}

async def _scheduler_loop(sid: str, payload: Dict[str, Any]):
    logger.info("Scheduler loop started for %s", sid)
    sched = SchedulerAgent()
    while True:
        session = sessions.get(sid)
        if not session:
            logger.info("Session not found, stopping loop for %s", sid)
            break
        if session.get("state") == "paused":
            await asyncio.sleep(1)
            continue
        plan = await sched.run(session["metadata"])
        logger.info("Scheduler planned: %s", plan)
        mem.add(session["user_id"], {"type": "plan", "content": plan})
        await asyncio.sleep(payload.get("reminder_interval", 60))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)