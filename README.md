# ACM Research Lab 26-27

## Week 4

### Overview

`week-4/calls.py` sends one prompt (a pancake recipe for four people with healthy substitutes explained) to two models through OpenRouter and saves the answers to `week-4/outputs.txt`.

### Models used
- `google/gemma-4-26b-a4b-it` (open-weight)
- `meta-llama/llama-3.1-8b-instruct` (open-weight)

### How to run

1. Install dependencies: `pip install openai python-dotenv`
2. Create a `.env` file in the repo root (it is git-ignored) containing: `OPENROUTER_API_KEY=your-key-here`
3. From the `week-4/` folder, run: `python calls.py`

## Week 5

### Overview

`week-5/murder_mystery.py` is a forward-chaining experiment that establishes a list of rules and derives whether a suspect is a prime suspect based on their clues. It also counts how many passes the loop takes to analyze the effect of reordering the rules. The output is saved to `week-5/outputs.txt`.

### How to run

1. From the `week-5/` folder, run: `python murder_mystery.py`.
2. To also save the printed output: `python murder_mystery.py | tee outputs.txt`