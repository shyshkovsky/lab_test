def dodavannya(x, y):
    return x + y

def vidnimannya(x, y):
    return x - y

def mnozhennya(x, y):
    return x * y

def dilennya(x, y):
    return x / y

print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

while True:
    вибір = input("Введіть номер операції (1/2/3/4): ")

    if вибір in ('1', '2', '3', '4'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if вибір == '1':
            print(num1, "+", num2, "=", dodavannya(num1, num2))

        elif вибір == '2':
            print(num1, "-", num2, "=", vidnimannya(num1, num2))

        elif вибір == '3':
            print(num1, "*", num2, "=", mnozhennya(num1, num2))

        elif вибір == '4':
            if num2 == 0:
                print("Помилка! Ділення на нуль не можливе!")
            else:
                print(num1, "/", num2, "=", dilennya(num1, num2))
        break
    else:
        print("Неправильний вибір!")
