import random
nums = [random.randint(-15, 15) for _ in range(10)]
print("Original:", nums)
print("Squared:", list(map(lambda x: x**2, nums)))
