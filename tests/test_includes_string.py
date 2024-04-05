from lib.includes_string import *

"""
Given a string that starts with the string `#TODO`
It returns True
"""
def test_starts_with_todo_return_true():
    expected = True
    actual = includes_string("#TODOhello WORLD")
    assert expected == actual

"""
Given a string that ends with the string `#TODO`
It returns True
"""
def test_ends_with_todo_return_true():
    expected = True
    actual = includes_string("hello WORLD#TODO")
    assert expected == actual

"""
Given a string that contains the string `#TODO` in the middle
It returns True
"""
def test_contains_todo_return_true():
    expected = True
    actual = includes_string("hello WORLD#TODO")
    assert expected == actual