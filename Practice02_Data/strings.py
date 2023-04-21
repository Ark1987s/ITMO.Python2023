# Работа с данными

# Работа со строками

STRING1 = " This is a string. "
STRING2 = "This is another string."

print(STRING1 + STRING2)

print(len(STRING1))
print(STRING1.title())
print(STRING1.lower())
print(STRING1.upper())
print(STRING1.rstrip())
print(STRING1.lstrip())
print(STRING1.strip())
print(STRING2.strip('!'))

# Извлечение символов и подстрок

first_symbol = STRING2[0]
print(first_symbol)
symbols1 = STRING1[1:3]
print(symbols1)
symbols1 = STRING1[1:]
print(symbols1)
symbols1 = STRING1[:3]
print(symbols1)
symbols1 = STRING1[:]
print(symbols1)
symbols1 = STRING1[1:20:2]
print(symbols1)