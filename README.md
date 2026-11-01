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

