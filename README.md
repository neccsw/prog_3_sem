# Programming, 3rd Semester

## Setup

Install `uv` and Python 3.14. For the notebook, install VS Code with the Python and Jupyter extensions.

Run this command from the repository root to install dependencies for every homework into the shared `.venv`:

```bash
uv sync --all-packages --locked
```

Run all commands below from the repository root as well. The `--directory` option sets the working directory needed by task modules; you do not need to activate `.venv` manually.

## Lecture Homework 1

### Task 1: Character count

Enter a line of text when prompted. The program prints its character count.

```bash
uv run --locked --package lect-hw1 --directory hw/lect/hw1/src python -m tasks.task1.main
```

### Task 2: Regular expressions

Enter a regular expression, then a line of text. The program prints the matches and their count.

```bash
uv run --locked --package lect-hw1 --directory hw/lect/hw1/src python -m tasks.task2.main
```

### Task 3: File statistics

Reads the bundled [text55.txt](hw/lect/hw1/data/text55.txt) and prints its contents and character, word, and line counts. No input is required.

```bash
uv run --locked --package lect-hw1 --directory hw/lect/hw1/src python -m tasks.task3.main
```

## Lecture Homework 2

This homework uses [Credential-security-project](https://github.com/neccsw/Credential-security-project) as a Git submodule. Initialize it before running Tasks 1 and 2:

```bash
git submodule update --init --recursive
```

For a fresh checkout, clone with submodules instead:

```bash
git clone --recurse-submodules https://github.com/neccsw/prog_3_sem.git
```

### Task 0: HTTP request

Sends a GET request to the GitHub API and prints the HTTP status code. Internet access is required.

```bash
uv run --locked --package lect-hw2 --directory hw/lect/hw2/src python -m tasks.task0.main
```

### Task 1: Password generator

Enter a name containing at least two Latin letters. The program generates a password of the same length using the submodule's HTTP API generator, then ensures an uppercase letter and a special character decoded from HEX. Internet access is required; API failures are reported without a local fallback.

```bash
uv run --locked --package lect-hw2 --directory hw/lect/hw2/src python -m tasks.task1.main
```

### Task 2: Custom module

Demonstrates the custom [password module](hw/lect/hw2/src/password.py) using `Natalia` and special characters decoded from the submodule's HEX data. No input or internet access is required.

```bash
uv run --locked --package lect-hw2 --directory hw/lect/hw2/src python -m tasks.task2.main
```

### Task 3: Three modules

Uses `random`, `math`, and `datetime` to print a random integer from 1 to 100, its square root, and the current local date. No input or internet access is required.

```bash
uv run --locked --package lect-hw2 --directory hw/lect/hw2/src python -m tasks.task3.main
```

## Practical Homework 1

An interactive Wordle game in [main.ipynb](hw/pract/hw1/main.ipynb).

1. Complete the setup above and open the repository in VS Code.
2. Open `hw/pract/hw1/main.ipynb`.
3. Use **Select Kernel** to choose the repository's `.venv/bin/python` interpreter. If it is not listed, use **Select Another Kernel → Python Environments** to locate it.
4. Skip the first cell (`!pip install colorama`): the workspace setup already installs `colorama`, `requests`, and `ipykernel`.
5. Run the game cell and answer its input prompts.

Internet access is required to fetch the word list. Enter `YES` to start, then enter five-letter words when prompted. You have six attempts to guess the word. At the replay prompt, enter `YES` to play again or `NO` to finish. The selected word varies between games.

## Practical Homework 2

Runs the text analyzer in [src/main.py](hw/pract/hw2/src/main.py) against the bundled [text.txt](hw/pract/hw2/data/text.txt). No input is required.

```bash
uv run --locked --package pract-hw2 python hw/pract/hw2/src/main.py
```

The output includes word frequencies, shortest and longest words, unique and total word counts, used letters, and the most frequent letters.

## Practical Homework 3

Run the task modules below. Random results vary between runs.

### Task 0: Random numbers

Prints a random decimal, a random integer in a range, and a randomly selected value.

```bash
uv run --locked --package pract-hw3 --directory hw/pract/hw3/src python -m tasks.task0.main
```

### Task 1: Random student

Selects one student from the bundled [studentList.csv](hw/pract/hw3/data/studentList.csv).

```bash
uv run --locked --package pract-hw3 --directory hw/pract/hw3/src python -m tasks.task1.main
```

### Task 2: Random student selections

Makes a random number of selections from the same CSV. Students can repeat, and a run can produce no selections.

```bash
uv run --locked --package pract-hw3 --directory hw/pract/hw3/src python -m tasks.task2.main
```

### Task 3: Coin flips

Simulates 10,000 coin flips and prints totals after 100, 1,000, and 10,000 flips.

```bash
uv run --locked --package pract-hw3 --directory hw/pract/hw3/src python -m tasks.task3.main
```

### Task 4: Higher or lower

Guess whether the next number will be higher or lower. Enter `higher` or `lower` when prompted, or `quit` (`q`) to finish early. The game lasts up to ten rounds; each correct full-word guess earns one point, and ties earn no points. Known issue: the accepted aliases `h` and `l` currently earn no points; use the full words for scoring.

```bash
uv run --locked --package pract-hw3 --directory hw/pract/hw3/src python -m tasks.task4.main
```
