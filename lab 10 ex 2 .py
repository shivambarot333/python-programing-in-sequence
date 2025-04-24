import csv

data_dict = {}
with open("marks.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = sum(int(row[sub]) for sub in ['Subject1', 'Subject2', 'Subject3'])
        data_dict[row['RollNo']] = {
            "Name": row['Name'],
            "Marks": [row['Subject1'], row['Subject2'], row['Subject3']],
            "Total": total
        }

print(data_dict)
