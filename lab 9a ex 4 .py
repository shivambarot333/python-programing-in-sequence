def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

# Example usage
print(reverse_list([1, 2, 3, 4, 5]))
