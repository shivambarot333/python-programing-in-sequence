def ispangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

# Example usage
print(ispangram("The quick brown fox jumps over the lazy dog"))
