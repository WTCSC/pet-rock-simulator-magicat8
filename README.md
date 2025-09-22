# Pet Rock Simulator

A tiny, terminal-based pet rock simulator written in Python. Name a rock, take care of it, and try to keep its hunger, happiness, energy, and health in a good range. Make choices each turn to feed, play, or do nothing — but watch the meters!

## Requirements

- Python 3.6+ (tested on Python 3.x)

There are no external dependencies.

## Running

Open a terminal in the repository folder and run:

```powershell
python .\pet_rock.py
```

On non-Windows shells use `python3` if `python` points to Python 2.

## How to play

When you run the script you'll be prompted for a name for your pet rock (default: "Rocky"). Each turn you'll see the rock's current stats:

- Happiness: 0–10
- Hunger: 0–10 (high is bad)
- Energy: 0–10
- Health: integer (starts at 10)

Actions:

- 1 — Feed the rock
  - Decreases hunger, slightly reduces happiness, increases energy
- 2 — Play with the rock
  - Increases happiness, increases hunger, decreases energy (may fail if energy is too low)
- 3 — Do nothing
  - Hunger increases, happiness decreases, energy recovers a bit
- 4 or `q`/`quit` — Quit the game

After each turn the game applies passive changes (hunger slowly increases, happiness drops, health may decrease if hunger is very high or happiness is very low). If any of the fail conditions are reached the game ends. Examples of game-over reasons include:

- Hunger reaches 10
- Happiness reaches 0
- Energy or Health reach 0

## Design notes

- The script uses simple integer stats clamped to sensible ranges.
- Health decreases when hunger is >= 8 or happiness is <= 2.

## Example session

You will be prompted for a name and shown a menu. Example (user input is shown after each prompt):

```
What will you name your pet rock? Rocky

--- Your Pet Rock, Rocky ---
Happiness: 5/10
Hunger: 5/10
Energy: 5/10

What do you want to do?
  1. Feed the rock
  2. Play with the rock
  3. Do nothing
  4. Quit
Your choice: 1

You fed your rock.
```

## Extending

This small script is a good starting point for learning to add features such as saving/loading, randomized events, item inventory, or a graphical frontend.

## License

This repository contains a short educational script. Use as you like.
