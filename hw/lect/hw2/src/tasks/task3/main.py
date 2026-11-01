import math
import random
from datetime import datetime


def main():
    number = random.randint(1, 100)

    print("Random number:", number)
    print("Square root:", math.sqrt(number))
    print("Date:", datetime.now().date())


if __name__ == "__main__":
    main()
