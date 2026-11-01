from handler import EmptyTextError

class analyzer:
    def analyze_text():
        text = str(input())

        if not text:
            raise EmptyTextError("Пустий текст")
        else:
            return len(text)