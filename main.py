"""
This file calls each of the functions defined in the other two files:
- practice_output.py
- practice_input.py

Run this file to see whether the code in each of the functions has the correct behavior.
- if you want to run just one function, comment out (i.e. disable) the calls to all the other functions
- put a # sign in front of the line with any function call you want to disable, e.g.:
    # practice_output.print_with_line_break()
"""

# import both files
import practice_output
import practice_input


def main():
    """
    Calls each of the functions in the practice_output and practice_input files
    """

    # call each function defined in practice_output
    practice_output.print_with_line_break()
    practice_output.print_without_line_break()
    practice_output.print_with_separator_dash_and_with_line_break()
    practice_output.print_with_separator_dash_and_without_line_break()

    # call each function defined in practice_input
    practice_input.get_favorite_vegetable()
    practice_input.get_favorite_number()
    practice_input.get_name_and_zodiac_sign()
    practice_input.get_name_and_age()


# run the code defined within the main function
main()
