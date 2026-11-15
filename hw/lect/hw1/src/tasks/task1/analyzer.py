from handler import EmptyTextError


def analyze_text():
    text = str(input())

    if not text:
        raise EmptyTextError("Пустий текст")
    else:
        return len(text)
