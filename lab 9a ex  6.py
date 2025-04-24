def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

# Example usage
print(sanitize_list([3, -1, 4, -5, 6]))
