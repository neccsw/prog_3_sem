import random
import string


class password:
    def validate_name(name):
        name = name.strip()

        if len(name) < 2 or any(
            character not in string.ascii_letters for character in name
        ):
            raise ValueError("Error: enter a name with at least two Latin letters.")

        return len(name)

    def get_special_characters():
        try:
            from credential_security_project.src.passImpr import PasswordImprover
        except ModuleNotFoundError as error:
            raise RuntimeError(
                "Error: initialize the submodule with "
                "git submodule update --init --recursive."
            ) from error

        try:
            characters = PasswordImprover("").get_random_character()
        except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
            raise RuntimeError(
                "Error: could not read the HEX special characters."
            ) from error

        if not characters or any(
            len(character) != 1 or character not in string.punctuation
            for character in characters
        ):
            raise RuntimeError("Error: invalid HEX special characters.")

        return characters

    def generate(length):
        if length < 2:
            raise ValueError("Error: password length must be at least two.")

        characters = password.get_special_characters()

        try:
            from credential_security_project.src.passGen import PasswordGenerator
        except ModuleNotFoundError as error:
            raise RuntimeError(
                "Error: initialize the submodule and install dependencies "
                "with uv sync --all-packages --locked."
            ) from error

        api_length = max(length, 4)

        try:
            generated = PasswordGenerator.generate(api_length)
        except (ValueError, AttributeError, TypeError) as error:
            raise RuntimeError("Error: invalid password generator response.") from error

        alphabet = string.ascii_letters + string.digits + string.punctuation
        if (
            not isinstance(generated, str)
            or len(generated) != api_length
            or any(character not in alphabet for character in generated)
        ):
            raise RuntimeError(
                "Error: could not generate a password of the requested length."
            )

        result = list(generated[:length])
        capital_index, special_index = random.sample(range(length), 2)
        result[capital_index] = random.choice(string.ascii_uppercase)
        result[special_index] = random.choice(characters)

        return "".join(result)
