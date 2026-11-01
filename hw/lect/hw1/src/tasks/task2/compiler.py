import handler
import re

class compiler:
    def compile():
        expression = str(input())

        if not expression:
            raise handler.EmptyTextError("Text is empty")

        try:
            return re.compile(expression)
        except re.error as error:
            raise handler.RegExSyntaxError("Regular expression has invalid syntax") from error

    def find_matches(expression):
        text = str(input())

        if not text:
            raise handler.EmptyTextError("Text is empty")

        return expression.findall(text)

