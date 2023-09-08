# Stacks
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or pairs[char] != stack.pop():
                return False
    return stack == []

# Sequences (Lists/Tuples)
def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Dictionaries
def word_frequency(sentence):
    sentence = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in sentence)
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Testing the functions
expression1 = "([]{})"
expression2 = "([)]"
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
sentence = "This is a test sentence. This sentence is a test."

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
print(remove_duplicates(input_sequence))  # Output: [2, 3, 4, 5, 6, 7]
print(word_frequency(sentence))
