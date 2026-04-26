# Simple Game — Python Project 2

A menu-driven mini game collection built in Python using functions and the `random` module.

---

## Games Included

- **Stone Paper Scissors** — Classic hand game against the computer
- **Dice Roll** — You and the computer each roll a dice; highest roll wins

---

## Project Structure

```
simple_game/
├── main.py       # Entry point — runs the menu loop and calls game functions
└── README.md
```

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python main.py
```

No external libraries required. Only the built-in `random` module is used.

---

## How It Works

### Menu
On launch, a menu is displayed in an infinite loop (`while True`). The user picks a game or exits.

### Stone Paper Scissors
- User picks Stone, Paper, or Scissors (1–3)
- Computer picks randomly using `random.choice()`
- Winner is decided by standard rules
- Invalid input is handled with `try/except`

### Dice Roll
- User presses Enter to roll
- Both user and computer get a random number from 1–6 via `random.randint()`
- Highest number wins; tie is possible

---

## Concepts Used

| Concept | Where |
|---|---|
| `random` module | Computer choice in both games |
| Functions | Each game and the menu are separate functions |
| `while True` loop | Keeps the menu running until user exits |
| `try/except` | Handles non-numeric and keyboard interrupt input |
| `if/elif/else` | Game result logic |

---

## Sample Output

```
Welcome to the Simple Game!

=== GAME MENU ===
1. Stone - Paper - Scissors
2. Dice Roll Game
3. Exit
================

Enter your choice (1-3): 1

=== Stone, Paper, Scissors ===
1. Stone
2. Paper
3. Scissors
Enter your choice (1-3): 1

You chose: Stone
Computer chose: Scissors
Result: You Win!
```

---

## Author

**Saurav**
B.Tech CSE — Chandigarh Engineering College (CGC)
Semester 2 — Python Programming Lab
