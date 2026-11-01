from .analyzer import analyzer
from handler import EmptyTextError

def main():
    print("Paste the text: ")

    attempt = True
    while(attempt):
        try:
            print(analyzer.analyze_text())
        except EmptyTextError as error:
            print(error)
        else:
            attempt = False
              


if __name__ == "__main__":
    main()
