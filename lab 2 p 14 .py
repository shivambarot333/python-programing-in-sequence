def calculate_grade(marks):
    if marks == -1:
        return "NA"
    elif marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    else:
        return "A+"

marks = []
for i in range(3):
    m = int(input(f"Enter marks for subject {i + 1} (-1 for Absent): "))
    marks.append(m)

if any(m <= 39 and m != -1 for m in marks):
    status = "Fail"
else:
    status = "Pass"

total = sum(m if m != -1 else 0 for m in marks)
average = total / 3
grades = [calculate_grade(m) for m in marks]

