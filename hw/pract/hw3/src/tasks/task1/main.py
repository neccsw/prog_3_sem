from pathlib import Path
import csv
import random


def main():
    studentList = Path(__file__).resolve().parents[3] / "data" / "studentList.csv"

    with open(studentList, mode="r", encoding="utf-8", newline="") as file:
        students = []

        for row in csv.reader(file):
            if row:
                students.append(row[0])

    print(random.choice(students))


if __name__ == "__main__":
    main()