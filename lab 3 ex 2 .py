# Convert to lowercase
def to_lower(s):
    new_str = ""
    for c in s:
        if 'A' <= c <= 'Z':  # If uppercase, convert to lowercase
            new_str += chr(ord(c) + 32)
        else:
            new_str += c  # Keep as is
    return new_str

# Convert to uppercase
def to_upper(s):
    new_str = ""
    for c in s:
        if 'a' <= c <= 'z':  # If lowercase, convert to uppercase
            new_str += chr(ord(c) - 32)
        else:
            new_str += c  # Keep as is
    return new_str

# Toggle case
def toggle_case(s):
    new_str = ""
    for c in s:
        if 'A' <= c <= 'Z':  # If uppercase, convert to lowercase
            new_str += chr(ord(c) + 32)
        elif 'a' <= c <= 'z':  # If lowercase, convert to uppercase
            new_str += chr(ord(c) - 32)
        else:
            new_str += c  # Keep as is
    return new_str

# Take user input
s = input("Enter a string: ")

# Print results
print("Lowercase:", to_lower(s))
print("Uppercase:", to_upper(s))
print("Toggle Case:", toggle_case(s))
