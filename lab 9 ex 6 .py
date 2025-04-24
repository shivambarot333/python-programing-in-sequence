def create_tuples_list(start, end):
    return [(x, x*2, x*3) for x in range(start, end + 1)]

# Example usage
print(create_tuples_list(1, 5))
