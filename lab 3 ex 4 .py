def remove_substring(main_str, remove_str):
    m, n = len(main_str), len(remove_str)
    
    # Loop to find the starting index of remove_str in main_str
    for i in range(m - n + 1):
        if main_str[i:i + n] == remove_str:
            return main_str[:i] + main_str[i + n:]  # Remove the substring
    
    return main_str  # Return original string if substring is not found

# Accept input from user
main_str = input("Enter the main string: ")
remove_str = input("Enter the string to remove: ")

# Print the modified string
print("Final string:", remove_substring(main_str, remove_str))
