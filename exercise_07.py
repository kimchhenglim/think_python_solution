def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.
    
    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!

def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.
    
    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

"""
Exercise 7.9.2
"""
def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True

"""
Exercise 7.9.3
"""
def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('cab', 'abc')
    False
    """
    for letter in word.lower():
        if letter.lower() not in available.lower():
                return True
            
    return False

"""
Exercise 7.9.4
"""
def uses_all(word, required):
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """

    for letter in required:
        if letter not in word:
            return False
        
    return True

"""
Exercise 7.9.5
"""
def check_word(word, available, required):
    """Check whether a word is acceptable.
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """

    word = str(word).lower()
    available = str(available).lower()
    required = str(required).lower()

    letter_count: int = 0
    is_required_found: bool = False

    for letter in word:
        if letter in available:
            if letter == required:
                is_required_found = True
            letter_count += 1
    
    if letter_count >= 4 and is_required_found:
        return True
    
    return False

def word_score(word, available):
    """Compute the score for an acceptable word.
    
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    word = str(word).lower()
    available = str(available).lower()

    is_pangram: bool = True
    letter_count: int = 0

    for letter in word:
        if letter in available:
            letter_count += 1

    for letter in available:
        if letter not in word:
            is_pangram = False

    score = 0

    if letter_count >= 4:
        score = (1 if letter_count == 4 else letter_count) + (7 if is_pangram else 0)

    return score

run_doctests(word_score)