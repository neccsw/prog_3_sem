import pandas as pd
from nltk.tokenize import RegexpTokenizer


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as error:
        raise FileNotFoundError("Error: file not found") from error
    except PermissionError as error:
        raise PermissionError("Error: permission denied") from error
    except UnicodeDecodeError as error:
        raise UnicodeDecodeError(
            error.encoding,
            error.object,
            error.start,
            error.end,
            "Error: file cannot be decoded as UTF-8",
        ) from error
    except OSError as error:
        raise OSError("Error: file cannot be read") from error


def normalize_text(text):
    text = text.lower()
    for apostrophe in "’‘ʼ":
        text = text.replace(apostrophe, "'")
    return text


def get_words(text):
    text = normalize_text(text)
    tokenizer = RegexpTokenizer(r"[a-zа-яіїєґё]+(?:['-][a-zа-яіїєґё]+)*")
    words = tokenizer.tokenize(text)
    if not words:
        raise ValueError("Error: text contains no words")
    return words


def count_words(text):
    return len(get_words(text))


def count_word_occurrences(text):
    words = get_words(text)
    word_counts = pd.Series(words).value_counts().to_dict()
    return dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
