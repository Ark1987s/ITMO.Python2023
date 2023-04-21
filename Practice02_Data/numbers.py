# Работа с числами
num1 = 3
num2 = 4
print(num2 / num1)
print(num2 % num1)
print(num2 ** num1)

# Преобразование данных
param = "string" + str(15)
print(param)

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(n1) + float(n2)
print("{:7.2f} + {:7.2f} = {:8.2f}".format(n1, n2, n3))

# Форматирование строк
a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))