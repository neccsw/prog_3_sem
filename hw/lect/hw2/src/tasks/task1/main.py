from password import password


def main():
    while True:
        name = input("Enter your name in Latin letters: ")

        try:
            length = password.validate_name(name)
        except ValueError as error:
            print(error)
        else:
            break

    try:
        generated = password.generate(length)
    except RuntimeError as error:
        print(error)
    else:
        print("Password length:", length)
        print("Password:", generated)


if __name__ == "__main__":
    main()
