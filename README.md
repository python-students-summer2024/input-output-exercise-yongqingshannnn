# Practicing Input and Output

This assignment will have you practice receiving text input from a user and producing text output to the Python command line.

## Details

This project includes some starter code as well as some tests that will help you determine whether you have written the solution code correctly or not.

### Starter code files

There are two starter code files:

- **practice_input.py**
- **practice_output.py**

And one program that, when run, will run all the code in both those `practice_` files.

- **main.py**

### Filling in the functions

Both `practice_*` files have some pre-defined functions. Each function has instructions for what code to write and place within it.

In order to properly place code within a function, the code within the function must be indented underneath the function definition.

For example, take this function starter code in the file, `practice_output.py`:

```python
def print_with_line_break():
  """
  Prints out the text, 'Hello world!' with a line break at the end
  """
  # write your code here
```

The code to solve this problem must be indented below the function definition, such as:

```python
def print_with_line_break():
  """
  Prints out the text, 'Hello world!' with a line break at the end
  """
  # write your code here
  print("Hello world!")
```

Note that the `print("Hello world!")` line is indented the same as the line above it, which is one tab to the right of the line that says, `def print_with_line_break():`. Keep this indentation.

### Running your programs

If you run the `practice_*` files directly, they will not actually do anything... none of the functions in those files are run, by default.

Run the given `main.py` file in order to run all the functions in the other two files.

If you want to only one run function at a time, comment out the calls to the other functions that you don't want to run. Python comments are lines that have the `#` in front of them - this disables those lines and prevents the interpreter from running them.

For example, if you only want to run the `print_with_line_break()` function from the `practice_output.py` file, your main function in `main.py` should look like this:

```python
def main():
  """
  Calls each of the functions in the practice_output and practice_input files
  """

  # call each function defined in practice_output
  practice_output.print_with_line_break()
  # practice_output.print_without_line_break()
  # practice_output.print_with_separator_dash_and_with_line_break()
  # practice_output.print_with_separator_dash_and_without_line_break()

  # call each function defined in practice_input
  # practice_input.get_favorite_vegetable()
  # practice_input.get_favorite_number()
  # practice_input.get_name_and_zodiac_sign()
  # practice_input.get_name_and_age()
```

### Testing your work

Included in the given code are some tests, using the **pytest** testing framework. These tests should all pass if the code in each function is done correctly.

If the tests do not appear, or seem to never stop loading, open up a Terminal window and run the command, `pytest --collect-only`, to see whether there are any errors in the code that prevent the tests from being discovered. If there are no errors reported from that command, try running the tests directly from the Terminal with the command, `pytest`.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
