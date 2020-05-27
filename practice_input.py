"""
A little assignment to practice receiving text
input from the user in Python.
"""

def get_favorite_vegetable():
  """
  Asks the user to enter their favorite vegetable
  and then prints out, "Interesting! I also love X!",
  where X is replaced with the user's favorite vegetable.
  """
  # write your code here.
  veggie = input("What's your favorite vegetable?")
  print("Interesting! I also love " + veggie + "!")

def get_favorite_number():
  """
  Asks the user to enter their favorite number
  and then prints out, "Interesting! I also love X!",
  where X is replaced with the user's favorite number.
  """
  # write your code here.
  num = input("What's your favorite number?")
  print("Interesting! I also love " + num + "!")

def get_name_and_zodiac_sign():
  """
  Asks the user to enter their name.
  Then ask them to enter their zodiac sign.
  Then print out, "Interesting! My name is also X, and I'm also a Y!",
  where X and Y are replaced by the user's name and zodiac sign, respectively.
  """
  # write your code here.
  name = input("What's your name?")
  sign = input("What's your zodiac sign?")
  print("Interesting! My name is also " + name + ", and I'm also a " + sign + "!")

def get_name_and_age():
  """
  Asks the user to enter their name.
  Then ask them to enter their age.
  Then print out, "Interesting! My name is also X, and I'm also Y years old!",
  where X and Y are replaced by the user's name and age, respectively.
  """
  # write your code here.
  name = input("What's your name?")
  age = input("What's your age?")
  print("Interesting! My name is also " + name + ", and I'm also " + str(age) + " years old!")

