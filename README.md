# QUIZ_GAME - ALL SAINT COLLEGE
# Quiz Game Project

## Overview
The **Quiz Game** is a Python-based console application designed for teenagers aged 13-19. It tests general knowledge through a series of five random questions. Players can score points by answering correctly and their progress is tracked in a CSV file.

## Features
- Interactive interface with detailed game instructions.
- Validates user eligibility based on age (13-19 years).
- Randomly selects questions from a predefined pool.
- Tracks player performance and maintains a leaderboard.
- Supports replay and displays the highest scores.
- Provides options to view or delete game records.

## Game Requirements
1. **Eligibility**: Only players aged 13-19 can participate.
2. **Required Information**:
   - Index Number
   - Name
   - Age
3. **Game Mechanics**:
   - Five rounds, each with one question.
   - Correct answers unlock the next question.
   - Each question is worth 20 points (maximum score: 100).
4. **Data Tracking**: Records are stored in `GAME_SUMMARY.csv`.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Quiz-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Quiz-Game
   ```
3. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Usage
1. Run the script:
   ```bash
   python QUIZ_GAME.py
   ```
2. Follow the prompts to enter your details and answer questions.
3. Choose options to replay or view/delete records at the end of the game.

## File Structure
- `QUIZ_GAME.py`: Main script for the game.
- `GAME_SUMMARY.csv`: Stores player data and scores (automatically generated).

## Sample Questions
- Who painted the "Mona Lisa"?
- Which planet is known as the Red Planet?
- What is the highest-grossing movie of all time?

## Future Improvements
- Add a graphical user interface (GUI).
- Expand the pool of questions.
- Include multiplayer functionality.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy playing and sharpening your general knowledge!


