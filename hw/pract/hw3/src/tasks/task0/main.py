import random

def main():
    x = -5
    y = 17
    z = 22.8

    print(f"Random number from 0 to 1 inclusively: {random.random()}")
    print(f"Random number from 'x' to 'y': {random.randint(x, y)}")
    print(f"Random number between x, y, and z: {random.choice([x, y, z])}")

if __name__ == "__main__":
    main()