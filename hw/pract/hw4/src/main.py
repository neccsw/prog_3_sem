import json
from pathlib import Path

import wer


def main():
    homework_path = Path(__file__).resolve().parents[1]
    result_path = homework_path / "results.json"

    try:
        reference = wer.read_file(homework_path / "data" / "reference.txt")
        hypothesis = wer.read_file(homework_path / "data" / "hypothesis.txt")
        metrics = wer.calculate(reference, hypothesis)
        with open(result_path, "w", encoding="utf-8") as file:
            json.dump(metrics, file, indent=4, ensure_ascii=False)
            file.write("\n")
    except (OSError, UnicodeDecodeError, ValueError) as error:
        print(error)
    else:
        for name, value in metrics.items():
            print(f"{name}: {value}")
        print(f"Results saved to: {result_path}")


if __name__ == "__main__":
    main()
