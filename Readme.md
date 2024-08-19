# Wordle Game
Guess the correct word in 6 attempts. After each guess, the tiles will show how close you are to the solution.
![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDJyaGFnMWd6a25nNXB3cTZhMzhtOGY1MDB6ZDB3OTM1N2NhMnFtaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ea1SPxvD1th2rUHePa/giphy.gif)

- **Green:** The letter is part of the word and in the correct position.
- **Yellow:** The letter is part of the word but in a different position.
- **Dark:** The letter is not part of the word.

Have fun!

## How to use

1. **Install requirements**: Open your terminal and run `pip install -r requirements.txt`
2. **Start the Game**: Run the script `main.py` to launch the wordle game window.


## Development Goals

- **Create GUI**: ✔️ 
- **Develop Game Logic**: ✔️
- **Implement Language Support for English and Portuguese**: ✔️
- **Add More Languages (e.g., Spanish, French, etc.)**: ☐
- **Implement a Solver Algorithm**: ☐ 

## Future Enhancements

1. **Multilingual Support**: Expand the game to include additional languages such as Spanish, French, and others. This will involve creating word lists and messages for each new language and integrating them into the game.
2. **Solver Algorithm**: Develop an algorithm to solve the game automatically. This enhancement will provide insights into solving strategies and improve gameplay analysis.

## Game Components

### Graphical User Interface (GUI)

- **Library Used**: Pygame
- **Purpose**: To create an interactive and visually appealing interface for the Wordle game.
- **Features**:
  - A grid where players can input their guesses.
  - Buttons for switching between languages (English and Portuguese).
  - Display of game results and error messages.
  - Dynamic updates based on user input and game state.

*Note: The GUI was created with the assistance of ChatGPT and the Pygame library documentation, which provided guidance on implementing the interface elements and handling game events.*

### Game Logic

- **Word Selection**: Randomly selects a word from a file based on the chosen language. Words are stored in text files, one for each supported language.
- **Word Verification**: Compares the guessed word with the target word and provides feedback on the correctness of each letter:
  - **Correct Letters**: Letters that match the target word's letters and their positions.
  - **Wrong Place Letters**: Letters that are in the target word but in the wrong position.
  - **Incorrect Letters**: Letters that are not present in the target word at all.
- **Word Existence Check**: Validates if the guessed word exists in the word list for the selected language. This ensures that the user can only submit valid guesses.

### Language Support

- **Current Languages**: English and Portuguese
- **Implementation**: Language-specific word lists and messages are used to provide a localized experience.
- **Goal**: To provide multilingual support, with initial implementation for English and Portuguese.