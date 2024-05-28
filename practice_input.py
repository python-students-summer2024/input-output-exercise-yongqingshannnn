"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
get_favorite_vegetable = input("what's your favorite vegetable?")
output_message = "Interesting! I also love" + get_favorite_vegetable +"!"
print(output_message)

def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
get_favorite_number = input("what's your favorite number?")
output_message = "Interesting! I also love" + get_favorite_number + "!"
print(output_message)


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
get_name = input("what's your name?")
get_zodiac_sign = input("what's your zodiac sign?")
output_message = "Interesting! My name is also" + get_name + ", and I'm also a" + get_zodiac_sign + "!"
print(output_message)
    


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
get_your_name = input("what is your name?")
get_age = input("how old are you?")
output_message = "Interesting! My name is also" + get_your_name + ", and I'm also" + get_age + "years old!"
print(output_message)

