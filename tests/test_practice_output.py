from practice_output import *


class Tests:
    def test_print_with_line_break(self, capsys):
        """
        Test that the method produces the correct output.
        """
        print_with_line_break()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Hello world!\n"
        assert (
            expected == actual
        ), f'Expected the print_with_line_break() function to print "{expected}"; instead, it printed "{actual}".'

    def test_print_without_line_break(self, capsys):
        """
        Test that the method produces the correct output.
        """
        print_without_line_break()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Hello world!"
        assert (
            expected == actual
        ), f'Expected the print_without_line_break() function to print "{expected}"; instead, it printed "{actual}".'

    def test_print_with_separator_dash_and_with_line_break(self, capsys):
        """
        Test that the method produces the correct output.
        """
        print_with_separator_dash_and_with_line_break()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Twas-brillig-and-the-slithy-toves\n"
        assert (
            expected == actual
        ), f'Expected the print_with_separator_dash_and_with_line_break() function to print "{expected}"; instead, it printed "{actual}".'

    def test_print_with_separator_dash_and_without_line_break(self, capsys):
        """
        Test that the method produces the correct output.
        """
        print_with_separator_dash_and_without_line_break()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Twas-brillig-and-the-slithy-toves"
        assert (
            expected == actual
        ), f'Expected the print_with_separator_dash_and_without_line_break() function to print "{expected}"; instead, it printed "{actual}".'
