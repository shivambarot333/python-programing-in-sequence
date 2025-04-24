def convert(s):
    words = sorted(set(s.split()))
    return ' '.join(words)

# Example usage
print(convert("banana apple orange banana grape apple"))
