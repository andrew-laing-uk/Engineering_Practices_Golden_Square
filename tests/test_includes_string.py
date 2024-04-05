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

"""
Given a string that does NOT contain the string `#TODO`
It returns False
"""
def test_does_not_contain_todo_return_false():
    expected = False
    actual = includes_string("hello WORLD")
    assert expected == actual

"""
Given an empty string
It returns False
"""
def test_empty_string_returns_false():
    expected = False
    actual = includes_string("")
    assert expected == actual