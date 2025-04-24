def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
print(ispalindrome("Madam In Eden Im Adam"))
