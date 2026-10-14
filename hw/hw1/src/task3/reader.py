import handler

class reader:
    def read_file(path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError as error:
            raise FileNotFoundError("Error: file not found") from error
        except PermissionError as error:
            raise handler.FilePermissionError("Error: permission denied") from error
        except UnicodeDecodeError as error:
            raise handler.FileDecodeError("Error: file cannot be decoded as UTF-8") from error

    def count_characters(text):
        return len(text)

    def count_words(text):
        return len(text.split())

    def count_lines(text):
        return len(text.splitlines())
