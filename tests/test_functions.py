from src.functions import is_balanced
from src.functions import word_frequency
from src.functions import remove_duplicates

def test_is_balanced():
    assert is_balanced("(([]){})") == True
    assert is_balanced("{[()]}") == True
    assert is_balanced("{[(])}") == False
    assert is_balanced("{{[[(())]]}}") == True
    assert is_balanced("}") == False

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []

def test_word_frequency():
    assert word_frequency("This is a test.") == {'this': 1, 'is': 1, 'a': 1, 'test': 1}
    assert word_frequency("Hello hello HELLO") == {'hello': 3}
    assert word_frequency("Punctuation, punctuation!") == {'punctuation': 2}
    assert word_frequency("") == {}
