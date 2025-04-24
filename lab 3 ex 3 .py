str1 = input("Enter the main string: ")
str2 = input("Enter the substring: ")

found = False
for i in range(len(str1) - len(str2) + 1):
    if str1[i:i+len(str2)] == str2:
        found = True
        break

if found:
    print("Yes, the substring is present.")
else:
    print("No, the substring is not present.")
