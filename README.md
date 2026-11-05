# 🏝️ MYSTERY ISLAND: THE LOST LIGHTHOUSE

## 1. Project Overview

Mystery Island: The Lost Lighthouse is a beginner-friendly, interactive Python text-adventure game.

The player wakes up stranded on a mysterious island following a terrible storm. The lighthouse beacon has gone dark, and the player must explore the island, collect useful objects, make decisions and restore the lighthouse beacon to escape.

The game uses text-based interaction through the Python terminal.

## 2. Project Objectives

The main objectives are to:

- Practise Python programming fundamentals.
- Understand variables, data types and user input.
- Apply conditional statements (`if`, `elif`, `else`).
- Understand loops and game control flow.
- Create and use lists for inventory management.
- Apply logical operators and membership checks.
- Handle invalid user input.
- Write automated tests using Python's `unittest` framework.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Testing Framework:** unittest
- **Development Environment:** Visual Studio Code (VS Code)
- **Version Control:** Git and GitHub

No external libraries, databases, graphical interfaces or AI APIs are required.

## 4. Project Structure

```text
Mystery-Island/
│
├── main.py
├── README.md
│
└── tests/
    ├── __init__.py
    └── test_main.py
```

### File descriptions

| File | Description |
|---|---|
| `main.py` | Contains the main game function, menu, player information, game decisions and replay mechanism. |
| `test_main.py` | Contains automated tests for important game behaviours. |
| `README.md` | Provides project documentation and instructions. |
| `__init__.py` | Allows the tests directory to be treated as a Python package. |

## 5. How to Install and Run

### Prerequisites

Install Python 3 on your computer.

Check your Python installation:

```bash
python --version
```

### Clone the repository

If the project is hosted on GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project folder:

```bash
cd Mystery-Island
```

### Run the game

Execute:

```bash
python main.py
```

Follow the instructions displayed in the terminal.

## 6. Game Rules and Instructions

### Starting the Game

When the game starts:

1. The game displays its title and introduction.
2. The player enters their name.
3. The player starts with five energy points.
4. The player's starting location is the Beach.
5. The inventory starts empty.

### Main Game Menu

The player receives six options:

| Option | Action |
|---|---|
| 1 | Explore the Jungle |
| 2 | Explore the Cave |
| 3 | Visit the Old Bridge |
| 4 | Visit the Lighthouse |
| 5 | Check Inventory |
| 6 | Quit Game |

### Collecting Objects

The player can collect two important objects:

**Rope**
- Found by searching the bushes in the Jungle.
- Required to cross the Old Bridge.
- Can only be collected once.

**Lantern**
- Found by searching the dark corner in the Cave.
- Required to restore the lighthouse beacon.
- Can only be collected once.

### Decisions and Consequences

The player encounters different decisions:

**Jungle**
- Search the bushes to find the Rope.
- Follow the mysterious sound and encounter a wild animal, losing additional energy.

**Cave**
- Search the dark corner to find the Lantern.
- Explore the narrow passage and encounter falling rocks, losing two energy points.

**Old Bridge**
- Cross carefully using the Rope, losing one energy point.
- Rush across the bridge, losing two energy points.

### Energy Management

The player starts with five energy points.

Energy decreases when performing certain actions.

When energy reaches zero, the player loses and the game ends.

### Winning the Game

To win:

1. Collect the Rope in the Jungle.
2. Collect the Lantern in the Cave.
3. Cross the Old Bridge.
4. Visit the Lighthouse.
5. Restore the lighthouse beacon using the required objects.

The game displays:

`CONGRATULATIONS! YOU WIN!`

### Losing the Game

The player loses when their energy reaches zero.

The game displays:

`GAME OVER! You have run out of energy.`

### Quitting and Replay

The player can select option 6 to quit.

After a game session, the program asks whether the player wants to play again.

A new call to `play_game()` creates fresh game variables.

## 7. Running Automated Tests

The project uses Python's built-in `unittest` framework.

The tests use:

- `unittest.TestCase` to organise tests.
- `unittest.mock.patch` to simulate player input.
- `redirect_stdout` to capture printed output.
- `StringIO` to store captured output for verification.
- `assertIn()` to check whether expected messages appear.
- `assertNotIn()` to check whether unwanted messages appear.

Run all tests from the main project directory:

```bash
python -m unittest discover -s tests -v
```

### Current Test Coverage

| Test | Expected Behaviour |
|---|---|
| Starting energy | Player begins with five energy points. |
| Invalid menu choice | Invalid menu input displays an error message. |
| Invalid Jungle choice | Invalid selection does not consume energy or collect Rope. |
| Invalid Cave choice | Invalid selection does not consume energy or collect Lantern. |
| Invalid Bridge choice | Invalid selection does not consume energy. |
| Winning path | Player can restore the lighthouse beacon and win. |

## 8. Known Limitations

The current version is an early playable implementation.

The following improvements are still needed:

1. Add a dedicated Beach exploration option.
2. Restrict movement according to the player's current location.
3. Prevent the player from visiting the Lighthouse without crossing the Old Bridge.
4. Improve energy management to ensure energy never becomes negative.
5. Prevent actions after the game has ended.
6. Add additional tests for duplicate item collection, energy exhaustion and replay.
7. Improve replay input validation.
8. Separate game logic from user interaction using dedicated functions and modules.

These improvements will be considered in subsequent development checkpoints.

## 9. Learning Outcomes

Through this project, I am practising:

- Creating and assigning variables.
- Working with strings, integers and lists.
- Collecting user input using `input()`.
- Displaying information using `print()`.
- Making decisions with conditional statements.
- Repeating actions using `while` loops.
- Defining and calling functions.
- Managing inventory using list membership.
- Handling invalid user input.
- Writing automated tests using `unittest`.

## 10. Conclusion

Mystery Island: The Lost Lighthouse is a practical Python learning project designed to strengthen programming fundamentals through interactive gameplay.

The project demonstrates how basic Python concepts can work together to create a simple text-based adventure.

The ultimate goal is not just to complete the game but to understand the logic behind every function, decision, loop and game mechanic.

**Project Status:** Beginner development / In progress.

**Author:** Ogah Samson Ogah.