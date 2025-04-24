def prime_factors(n, i=2):
    if n <= 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)

# Example usage
print(prime_factors(60))  # Output: [2, 2, 3, 5]
