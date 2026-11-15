import pytest

import analyzer
import main


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, world! HELLO.", {"hello": 2, "world": 1}),
        (
            "Мова єднає людей. МОВА єднає світ.",
            {"мова": 2, "єднає": 2, "людей": 1, "світ": 1},
        ),
        ("Hello, МОВА! hello 2026.", {"hello": 2, "мова": 1}),
        ("Цитата: «вежливые люди».", {"цитата": 1, "вежливые": 1, "люди": 1}),
        (
            "Ґанок Єнот Їжак Іній Йод",
            {"ґанок": 1, "єнот": 1, "їжак": 1, "іній": 1, "йод": 1},
        ),
    ],
)
def test_word_count_and_frequencies(text, expected):
    frequencies = analyzer.count_word_occurrences(text)
    assert frequencies == expected
    assert analyzer.count_words(text) == sum(expected.values())
    assert all(type(count) is int for count in frequencies.values())


def test_frequency_order():
    frequencies = analyzer.count_word_occurrences("zebra apple zebra apple banana")
    assert list(frequencies.items()) == [("apple", 2), ("zebra", 2), ("banana", 1)]


def test_apostrophes_and_hyphens():
    text = "П'ЯТЬ п’ять пʼять п‘ять будь-який don't 'слово' --текст--"
    assert analyzer.get_words(text) == [
        "п'ять",
        "п'ять",
        "п'ять",
        "п'ять",
        "будь-який",
        "don't",
        "слово",
        "текст",
    ]
    assert analyzer.count_word_occurrences(text)["п'ять"] == 4


@pytest.mark.parametrize("text", ["", " \t\n", "123 ...?!"])
def test_text_without_words(text):
    with pytest.raises(ValueError, match="text contains no words"):
        analyzer.count_words(text)
    with pytest.raises(ValueError, match="text contains no words"):
        analyzer.count_word_occurrences(text)


def test_read_utf8_file(tmp_path):
    file_path = tmp_path / "text.txt"
    file_path.write_text("Мова мова Hello", encoding="utf-8")
    text = analyzer.read_file(file_path)
    assert text == "Мова мова Hello"
    assert analyzer.count_words(text) == 3
    assert analyzer.count_word_occurrences(text) == {"мова": 2, "hello": 1}


def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="text contains no words"):
        analyzer.count_words(analyzer.read_file(file_path))


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="file not found"):
        analyzer.read_file(tmp_path / "missing.txt")


def test_invalid_encoding(tmp_path):
    file_path = tmp_path / "invalid.txt"
    file_path.write_bytes(b"\xff\xfe\xfa")
    with pytest.raises(UnicodeDecodeError, match="cannot be decoded as UTF-8"):
        analyzer.read_file(file_path)


@pytest.mark.parametrize(
    "error, expected_type, message",
    [
        (PermissionError("denied"), PermissionError, "permission denied"),
        (OSError("unavailable"), OSError, "file cannot be read"),
    ],
)
def test_reading_errors(monkeypatch, error, expected_type, message):
    def fail_to_open(*args, **kwargs):
        raise error

    monkeypatch.setattr("builtins.open", fail_to_open)
    with pytest.raises(expected_type, match=message):
        analyzer.read_file("text.txt")


def test_main_output(monkeypatch, capsys):
    monkeypatch.setattr(analyzer, "read_file", lambda path: "Hello world hello")
    main.main()
    assert capsys.readouterr().out == (
        "Words count: 3\nWord frequencies:\nhello: 2\nworld: 1\n"
    )


@pytest.mark.parametrize("error", [ValueError("empty text"), OSError("read error")])
def test_main_reports_errors(monkeypatch, capsys, error):
    def fail_to_read(path):
        raise error

    monkeypatch.setattr(analyzer, "read_file", fail_to_read)
    main.main()
    assert capsys.readouterr().out == f"{error}\n"
