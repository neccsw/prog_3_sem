from pathlib import Path
import handler
from .reader import reader

def main():
    file_path = Path(__file__).resolve().parents[3] / "data" / "text55.txt"

    try:
        text = reader.read_file(file_path)
    except FileNotFoundError as error:
        print(error)
    except handler.FilePermissionError as error:
        print(error)
    except handler.FileDecodeError as error:
        print(error)
    else:
        print(text)
        print("Characters count:", reader.count_characters(text))
        print("Words count:", reader.count_words(text))
        print("Lines count:", reader.count_lines(text))


if __name__ == "__main__":
    main()
