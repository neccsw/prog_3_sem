class analyzer:
    def read_file(path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError as error:
            raise FileNotFoundError("Error: file not found") from error
        except PermissionError as error:
            raise PermissionError("Error: permission denied") from error
        except UnicodeDecodeError as error:
            raise UnicodeDecodeError(
                error.encoding,
                error.object,
                error.start,
                error.end,
                "Error: file cannot be decoded as UTF-8",
            ) from error
        except OSError as error:
            raise OSError("Error: file cannot be read") from error

    def normalize_text(text):
        text = text.lower()
        for apostrophe in "’‘ʼ":
            text = text.replace(apostrophe, "'")
        return text

    def get_words(text):
        text = analyzer.normalize_text(text)
        words = []
        word = ""

        for index, character in enumerate(text):
            if character.isalpha() or (
                character in "'-"
                and word
                and word[-1].isalpha()
                and index + 1 < len(text)
                and text[index + 1].isalpha()
            ):
                word += character
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        return words

    def count_word_occurrences(text):
        word_counts = {}
        for word in analyzer.get_words(text):
            word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    def count_letter_occurrences(text):
        letter_counts = {}
        for letter in analyzer.normalize_text(text):
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
        return letter_counts

    def frequency_dictionary(text):
        word_counts = analyzer.count_word_occurrences(text)
        total = sum(word_counts.values())
        frequencies = {}

        for word, count in word_counts.items():
            frequencies[word] = count / total * 100

        return frequencies

    def shortest_words(text):
        word_counts = analyzer.count_word_occurrences(text)
        if not word_counts:
            return []

        shortest_length = len(min(word_counts, key=len))
        words = []
        for word in word_counts:
            if len(word) == shortest_length:
                words.append(word)
        return words

    def longest_words(text):
        word_counts = analyzer.count_word_occurrences(text)
        if not word_counts:
            return []

        longest_length = len(max(word_counts, key=len))
        words = []
        for word in word_counts:
            if len(word) == longest_length:
                words.append(word)
        return words

    def count_unique_words(text):
        return len(analyzer.count_word_occurrences(text))

    def count_words(text):
        return sum(analyzer.count_word_occurrences(text).values())

    def used_letters(text):
        return list(analyzer.count_letter_occurrences(text))

    def most_frequent_letters(text):
        letter_counts = analyzer.count_letter_occurrences(text)
        if not letter_counts:
            return []

        highest_count = max(letter_counts.values())
        letters = []
        for letter, count in letter_counts.items():
            if count == highest_count:
                letters.append(letter)
        return letters
