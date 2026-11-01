from password import password


def main():
    name = "Natalia"

    try:
        length = password.validate_name(name)
        characters = password.get_special_characters()
    except (ValueError, RuntimeError) as error:
        print(error)
    else:
        print("Name:", name)
        print("Password length:", length)
        print("Special characters from HEX codes:", " ".join(characters))


if __name__ == "__main__":
    main()
