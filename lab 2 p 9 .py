def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num
number = float(input("Enter a number: "))
print(f"The absolute value of {number} is {absolute_value(number)}")
