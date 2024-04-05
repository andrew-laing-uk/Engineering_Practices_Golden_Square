# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

def includes_string(str)

```python
# EXAMPLE

def includes_string(str):
    """Check if a text includes the string `#TODO`

    Parameters: (list all parameters and their types)
        str: a string to check if it includes the string `#TODO`

    Returns: (state the return value and its type)
        a boolean, True if str includes the string `#TODO`, otherwise False
    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string that starts with the string `#TODO`
It returns True
"""
includes_string("#TODOhello WORLD") => True


"""
Given a string that ends with the string `#TODO`
It returns True
"""
includes_string("hello WORLD#TODO") => True


"""
Given a string that econtains the string `#TODO`
It returns True
"""
includes_string("hello #TODO WORLD") => True


"""
Given a string that contains the string `#TODO`
It returns True
"""
includes_string("hello #TODO WORLD") => True


"""
Given a string that does NOT contain the string `#TODO`
It returns False
"""
includes_string("hello WORLD") => True

"""
Given an empty string
It returns False
"""
includes_string("hello WORLD") => True

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

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
includes_string("hello WORLD") => True

"""
Given an empty string
It returns False
"""
includes_string("hello WORLD") => True
```

Ensure all test function names are unique, otherwise pytest will ignore them!
