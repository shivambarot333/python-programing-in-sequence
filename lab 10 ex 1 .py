import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 24, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 22, "Delhi"]
]

with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
