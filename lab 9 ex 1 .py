def count_lower_upper(s):
    result = {'lowercase': 0, 'uppercase': 0}
    for char in s:
        if char.islower():
            result['lowercase'] += 1
        elif char.isupper():
            result['uppercase'] += 1
    return result

# Example usage
print(count_lower_upper("Hello World! Python123"))
