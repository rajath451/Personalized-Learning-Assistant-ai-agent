# API Documentation for Personalized Learning Assistant

## Overview
The Personalized Learning Assistant provides a set of APIs to interact with various collaborative agents designed to enhance the learning experience. The main agents include the Quiz Agent, Explanation Agent, and Scheduler Agent, each serving distinct roles in the learning process.

## Base URL
The base URL for all API endpoints is:
```
http://localhost:5000/api
```

## Endpoints

### Quiz Agent

#### Generate Quiz
- **Endpoint:** `/quiz/generate`
- **Method:** `POST`
- **Description:** Generates a quiz based on the user's profile and preferences.
- **Request Body:**
  ```json
  {
    "user_id": "string",
    "topic": "string",
    "difficulty": "string"
  }
  ```
- **Response:**
  ```json
  {
    "quiz_id": "string",
    "questions": [
      {
        "question": "string",
        "options": ["string"],
        "correct_answer": "string"
      }
    ]
  }
  ```

#### Submit Answers
- **Endpoint:** `/quiz/submit`
- **Method:** `POST`
- **Description:** Submits user answers for evaluation.
- **Request Body:**
  ```json
  {
    "quiz_id": "string",
    "user_id": "string",
    "answers": {
      "question_id": "string",
      "selected_option": "string"
    }
  }
  ```
- **Response:**
  ```json
  {
    "score": "integer",
    "feedback": "string"
  }
  ```

### Explanation Agent

#### Get Explanation
- **Endpoint:** `/explanation/get`
- **Method:** `POST`
- **Description:** Retrieves an explanation for a given concept.
- **Request Body:**
  ```json
  {
    "user_id": "string",
    "concept": "string"
  }
  ```
- **Response:**
  ```json
  {
    "concept": "string",
    "explanation": "string"
  }
  ```

### Scheduler Agent

#### Schedule Study Session
- **Endpoint:** `/scheduler/schedule`
- **Method:** `POST`
- **Description:** Schedules a study session for the user.
- **Request Body:**
  ```json
  {
    "user_id": "string",
    "subject": "string",
    "date_time": "string"
  }
  ```
- **Response:**
  ```json
  {
    "session_id": "string",
    "status": "string"
  }
  ```

#### Get Schedule
- **Endpoint:** `/scheduler/get`
- **Method:** `GET`
- **Description:** Retrieves the user's study schedule.
- **Query Parameters:**
  - `user_id`: `string`
- **Response:**
  ```json
  {
    "sessions": [
      {
        "session_id": "string",
        "subject": "string",
        "date_time": "string"
      }
    ]
  }
  ```

## Error Handling
All endpoints will return appropriate HTTP status codes and error messages in the following format:
```json
{
  "error": "string",
  "message": "string"
}
```

## Conclusion
This API documentation provides a comprehensive overview of the endpoints available in the Personalized Learning Assistant. Each agent's functionality is designed to work collaboratively to enhance the user's learning experience through quizzes, explanations, and scheduling.