lst = ['madam', 'Python', 'malayalam', 12321]
print(list(filter(lambda x: str(x) == str(x)[::-1], lst)))
