# Personalized Learning Assistant

## Overview
The Personalized Learning Assistant is an innovative application designed to enhance the learning experience through the use of collaborative agents. These agents work together to provide quizzes, explanations, and scheduling assistance tailored to individual user needs.

## Features
- **Collaborative Agents**: 
  - **Quiz Agent**: Generates practice questions and evaluates user responses.
  - **Explanation Agent**: Simplifies concepts and provides detailed explanations based on user queries.
  - **Scheduler Agent**: Plans study sessions and manages user schedules.

- **Adaptive Feedback**: The system adapts feedback based on user performance and interactions with the agents, ensuring a personalized learning journey.

- **Web Frontend**: A user-friendly web interface that allows users to interact with the agents seamlessly.

## Project Structure
```
personalized-learning-assistant
├── src
│   ├── main.py
│   ├── agents
│   ├── core
│   ├── api
│   ├── models
│   └── web
├── frontend
│   ├── package.json
│   ├── src
│   └── public
├── tests
├── docs
├── scripts
├── requirements.txt
├── pyproject.toml
├── .env.example
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd personalized-learning-assistant
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the frontend:
   ```
   cd frontend
   npm install
   ```

## Usage
To start the application, run the following command in the `src` directory:
```
python main.py
```
Then, navigate to `http://localhost:5000` in your web browser to access the application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.