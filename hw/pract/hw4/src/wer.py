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
    words = []
    word = ""

    for index, character in enumerate(text):
        if character.isalpha() or (
            character in "'-"
            and word
            and word[-1].isalpha()
            and index + 1 < len(text)
            and text[index + 1].isalpha()
        ):
            word += character
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    return words


def calculate(reference, hypothesis):
    reference = get_words(reference)
    hypothesis = get_words(hypothesis)
    if not reference:
        raise ValueError("Error: reference text contains no words")

    distances = [list(range(len(hypothesis) + 1))]
    for row in range(1, len(reference) + 1):
        distances.append([row] + [0] * len(hypothesis))
        for column in range(1, len(hypothesis) + 1):
            cost = int(reference[row - 1] != hypothesis[column - 1])
            distances[row][column] = min(
                distances[row - 1][column - 1] + cost,
                distances[row - 1][column] + 1,
                distances[row][column - 1] + 1,
            )

    substitutions = deletions = insertions = 0
    row, column = len(reference), len(hypothesis)
    while row or column:
        if row and column and reference[row - 1] == hypothesis[column - 1]:
            row -= 1
            column -= 1
        elif row and column and (
            distances[row][column] == distances[row - 1][column - 1] + 1
        ):
            substitutions += 1
            row -= 1
            column -= 1
        elif row and distances[row][column] == distances[row - 1][column] + 1:
            deletions += 1
            row -= 1
        else:
            insertions += 1
            column -= 1

    return {
        "WER": (substitutions + deletions + insertions) / len(reference),
        "S": substitutions,
        "D": deletions,
        "I": insertions,
        "N": len(reference),
    }
