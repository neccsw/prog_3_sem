import handler
from .compiler import compiler

def main():
    print("Paste the regular expression: ")

    attempt = True
    while(attempt):
        try:
            expression = compiler.compile()
        except handler.RegExSyntaxError as error:
            print(error)
        except handler.EmptyTextError as error:
            print(error)
        else:
            attempt = False

    print("Paste the text: ")

    attempt = True
    while(attempt):
        try:
            matches = compiler.find_matches(expression)
        except handler.EmptyTextError as error:
            print(error)
        else:
            print("Matches:", matches)
            print("Matches count:", len(matches))
            attempt = False


if __name__ == "__main__":
    main()
