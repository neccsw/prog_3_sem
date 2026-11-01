from pathlib import Path

from analyzer import analyzer


def main():
    file_path = Path(__file__).resolve().parents[1] / "data" / "text.txt"

    try:
        text = analyzer.read_file(file_path)
    except (OSError, UnicodeDecodeError) as error:
        print(error)
    else:
        print("Word frequencies:")
        for word, percentage in analyzer.frequency_dictionary(text).items():
            print(f"{word}: {percentage:.2f}%")
        print("Shortest words:", analyzer.shortest_words(text))
        print("Longest words:", analyzer.longest_words(text))
        print("Unique words count:", analyzer.count_unique_words(text))
        print("Words count:", analyzer.count_words(text))
        print("Used letters:", analyzer.used_letters(text))
        print("Most frequent letters:", analyzer.most_frequent_letters(text))


if __name__ == "__main__":
    main()
