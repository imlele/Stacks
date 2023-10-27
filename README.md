# Stacks

A brief description of your game and AI solver. What's the main goal of the game, and what was the main challenge in creating the AI solver?

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [AI Solver](#ai-solver)
- [License](#license)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/imlele/Stacks.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Stacks
   ```


## Usage

1. **Custom Game**: 
   ``` bash
   py main.py
   ```
2. **AI Solver**: 
   ``` bash
   py solution.py
   ```

## Game Rules

1. **Objective:** The main goal is to organize chips into stacks such that each stack contains chips of only one color.

2. **Stack Rules**:

   - Each stack has a maximum capacity defined by `STACK_MAX`.
   - Chips can only be moved onto stacks where the top chip matches the color of the moving chips.
   - When moving chips, all consecutive chips of the same color must be moved together.
   - The sum of moving chips and those in the destination stack should not exceed the stack's `STACK_MAX`.
   - Any color chips can be placed in an empty stack, but they must still adhere to the stacking rules.
   - If both the origin and destination stacks have the same color chips, you can transfer chips until the destination stack is full.

## AI Solver

1. **Objective**: The AI aims to determine the optimal move at each step to maximize the `purity` of the game's stacks.

2. **Best Move Selection**:
   - For each possible move from the current state:
     - A child game state is created by simulating the move.
     - If this state has been visited before, it's skipped.
     - The child state's purity is evaluated.
   - The move leading to the highest increase in purity is selected as the best move.

3. **State Representation**:
   - Each game state is uniquely identified using a hash, derived from its string representation.
   - A set, `states`, records all visited states, ensuring no repetition in game state exploration.

4. **Solver Logic**:
   - The AI continuously chooses and applies the best move.
   - If no available move can improve the game state, the AI adds a new empty stack and re-evaluates the best move.
   - The process repeats until the game reaches its final, most pure state.

## License

## To-Do:

The following is a list of enhancements and features that we aim to implement in upcoming versions:

- **Improved AI Efficiency**: Work on optimizing the AI algorithms for faster and smarter gameplay solutions.
  
- **User Interface Enhancements**: Introduce a graphical user interface (GUI) for a more interactive and intuitive gameplay experience.
   
- **Dynamic Difficulty Levels**: Offer varying levels of gameplay difficulty, adapting to the player's proficiency and providing an evolving challenge.
  
- **Custom Game Modes**: Provide options for users to customize stack and chip parameters, giving a personalized touch to the gameplay.
  
- **Feedback Mechanism**: Introduce a system for players to provide feedback, report bugs, or suggest new features.
  
- **Tutorials & Guides**: Develop comprehensive tutorials and guides to assist newcomers in understanding game mechanics and strategies.
