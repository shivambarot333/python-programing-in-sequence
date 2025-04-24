def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Example usage
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
