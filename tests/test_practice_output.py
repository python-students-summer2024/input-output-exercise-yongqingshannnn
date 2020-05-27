
from practice_output import *

class Tests:

  def test_print_with_line_break(self, capsys):
    """
    Test that the method produces the correct output.
    """
    print_with_line_break()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!\n"

  def test_print_without_line_break(self, capsys):
    """
    Test that the method produces the correct output.
    """
    print_without_line_break()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!"

  def test_print_with_separator_dash_and_with_line_break(self, capsys):
    """
    Test that the method produces the correct output.
    """
    print_with_separator_dash_and_with_line_break()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Twas-brillig-and-the-slithy-toves\n"

  def test_print_with_separator_dash_and_without_line_break(self, capsys):
    """
    Test that the method produces the correct output.
    """
    print_with_separator_dash_and_without_line_break()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Twas-brillig-and-the-slithy-toves"

  def test_main(self, capsys):
    """
    Test the main method
    """
    main()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!\nHello world!Twas-brillig-and-the-slithy-toves\nTwas-brillig-and-the-slithy-toves"
