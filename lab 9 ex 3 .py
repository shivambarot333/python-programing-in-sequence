def create_array(x, y, z, val):
    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

# Example usage
array_3d = create_array(3, 4, 5, 7)
print(array_3d)
