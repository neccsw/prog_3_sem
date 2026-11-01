import random


def main():
    print("Guess whether the next number from 1 to 100 will be higher or lower.")
    print("You have 10 rounds. Each correct guess earns 1 point.")
    print("Equal numbers count as a round and earn no points.")
    print("Enter higher, lower, or quit to finish early.")

    current_number = random.randint(1, 100)
    score = 0
    completed_rounds = 0

    for round_number in range(1, 11):
        print(f"\nRound {round_number}/10 | Score: {score}")
        print(f"Current number: {current_number}")

        while True:
            guess = input("Your guess (higher/lower/quit): ").strip().lower()

            if guess == "quit" or guess == "q":
                print(f"Final score: {score}/10")
                print(f"Completed rounds: {completed_rounds}/10")
                return

            if guess in ("higher", "lower", "h", "l"):
                break

            print("Invalid command. Enter higher, lower, or quit.")

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        if next_number == current_number:
            print("It's a tie! No points this round.")
        elif (guess == "higher" and next_number > current_number) or (
            guess == "lower" and next_number < current_number
        ):
            score += 1
            print("Correct! You earned 1 point.")
        else:
            print("Incorrect! No points this round.")

        completed_rounds += 1
        current_number = next_number
        print(f"Score: {score}")

    print(f"\nFinal score: {score}/10")
    print(f"Completed rounds: {completed_rounds}/10")


if __name__ == "__main__":
    main()
