def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

# Example usage
print(string_length("Hello World"))  # Output: 11
