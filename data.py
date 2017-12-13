num1 = int(input("Input first digital "))
num2 = int(input("Input second digital "))
act = input("Input action ")
result = ''

def summ(x, y):
    if act == '+':
        return x + y
    if act == '-':
        return x - y
    if act == '*':
        return x * y
    if act == '/':
        return x / y



if act == '+':
    result = summ(num1, num2)
    print(result)

if act == '-':
    result = summ(num1, num2)
    print(result)


