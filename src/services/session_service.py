class InMemorySessionService:
    def __init__(self):
        self.sessions = {}

    def create(self, user_id: str, metadata: dict) -> str:
        sid = f"{user_id}-{len(self.sessions)+1}"
        self.sessions[sid] = {"user_id": user_id, "metadata": metadata, "state": "active"}
        return sid

    def get(self, sid: str):
        return self.sessions.get(sid)

    def pause(self, sid: str):
        if sid in self.sessions:
            self.sessions[sid]["state"] = "paused"

    def resume(self, sid: str):
        if sid in self.sessions:
            self.sessions[sid]["state"] = "active"

    def delete(self, sid: str):
        self.sessions.pop(sid, None)