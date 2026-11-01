import random

def main():
    tales = 0
    heads = 0

    for i in range(10000):
        flip = random.random()
        
        if flip < 0.5:
            tales += 1
        else:
            heads += 1

        if i == 99:
            print(f"Tales: {tales}, Heads: {heads}")

        if i == 999:
                    print(f"Tales: {tales}, Heads: {heads}")

    print(f"Tales: {tales}, Heads: {heads}")

if __name__ == "__main__":
    main()