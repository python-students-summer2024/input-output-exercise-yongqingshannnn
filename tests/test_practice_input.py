import unittest
#import mock
#import builtins
from practice_input import *

class Tests:

  def test_get_favorite_vegetable(self, capsys, monkeypatch):
    """
    Test that the method produces the correct output.
    """
    # Override the Python built-in input method 
    #with mock.patch.object(builtins, 'input', lambda: 'arugula'):
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    get_favorite_vegetable()
    captured = capsys.readouterr() # capture print output
    assert "Interesting! I also love arugula!" in captured.out
    
  def test_get_favorite_number(self, capsys, monkeypatch):
    """
    Test that the method produces the correct output.
    """
    # Override the Python built-in input method 
    #with mock.patch.object(builtins, 'input', lambda: 'arugula'):
    monkeypatch.setattr('builtins.input', lambda x: "3")
    get_favorite_number()
    captured = capsys.readouterr() # capture print output
    assert "Interesting! I also love 3!" in captured.out
    
  def test_get_name_and_age(self, capsys, monkeypatch):
    """
    Test that the method produces the correct output.
    """
    # Override the Python built-in input method 
    #with mock.patch.object(builtins, 'input', lambda: 'arugula'):
    monkeypatch.setattr('builtins.input', lambda x: "Bob")
    get_name_and_age()
    captured = capsys.readouterr() # capture print output
    assert "Interesting! My name is also Bob, and I'm also Bob years old!" in captured.out
    
  def test_get_name_and_zodiac_sign(self, capsys, monkeypatch):
    """
    Test that the method produces the correct output.
    """
    # Override the Python built-in input method 
    #with mock.patch.object(builtins, 'input', lambda: 'arugula'):
    monkeypatch.setattr('builtins.input', lambda x: "libra")
    get_name_and_zodiac_sign()
    captured = capsys.readouterr() # capture print output
    assert "Interesting! My name is also libra, and I'm also a libra!" in captured.out
    
     
if __name__ == '__main__':
    unittest.main()