from practice_input import *


class Tests:
    def test_get_favorite_vegetable(self, capsys, monkeypatch):
        """
        Test that the method produces the correct output.
        """
        # Override the Python built-in input method
        mock_data = "arugula"
        monkeypatch.setattr("builtins.input", lambda x: mock_data)
        get_favorite_vegetable()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Interesting! I also love arugula!"
        assert (
            expected in actual
        ), f'Expected the printed output of the get_favorite_vegetable() function call to contain the text, "{expected}" when the user inputs the response, "{mock_data}"; instead, the printed output was, "{actual}".'

    def test_get_favorite_number(self, capsys, monkeypatch):
        """
        Test that the method produces the correct output.
        """
        # Override the Python built-in input method
        mock_data = "3"
        monkeypatch.setattr("builtins.input", lambda x: mock_data)
        get_favorite_number()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Interesting! I also love 3!"
        assert (
            expected in actual
        ), f'Expected the printed output of the get_favorite_number() function call to contain the text, "{expected}" when the user inputs the response, "{mock_data}"; instead, the printed output was, "{actual}".'

    def test_get_name_and_age(self, capsys, monkeypatch):
        """
        Test that the method produces the correct output.
        """
        # Override the Python built-in input method
        mock_data = "Bob"
        monkeypatch.setattr("builtins.input", lambda x: mock_data)
        get_name_and_age()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Interesting! My name is also Bob, and I'm also Bob years old!"
        assert (
            expected in actual
        ), f'Expected the printed output of the get_name_and_age() function call to contain the text, "{expected}" when the user inputs the response, "{mock_data}"; instead, the printed output was, "{actual}".'

    def test_get_name_and_zodiac_sign(self, capsys, monkeypatch):
        """
        Test that the method produces the correct output.
        """
        # Override the Python built-in input method
        mock_data = "libra"
        monkeypatch.setattr("builtins.input", lambda x: mock_data)
        get_name_and_zodiac_sign()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Interesting! My name is also libra, and I'm also a libra!"
        assert (
            expected in actual
        ), f'Expected the printed output of the get_name_and_zodiac_sign() function call to contain the text, "{expected}" when the user inputs the response, "{mock_data}"; instead, the printed output was, "{actual}".'
