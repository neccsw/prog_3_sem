from pathlib import Path

import analyzer


def main():
    file_path = Path(__file__).resolve().parents[1] / "data" / "text.txt"

    try:
        text = analyzer.read_file(file_path)
        word_count = analyzer.count_words(text)
        word_counts = analyzer.count_word_occurrences(text)
    except (OSError, UnicodeDecodeError, ValueError) as error:
        print(error)
    else:
        print("Words count:", word_count)
        print("Word frequencies:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
