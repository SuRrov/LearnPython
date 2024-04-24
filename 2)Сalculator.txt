print('Привет пользователь!!!  Я Калькулятор. \nЯ умею складывать,вычитать,умножать и делить числа. (+,-,*,/)')

Action = str(input("Введи действие над числами: "))

FirstNumber = int(input("Введи первое число: "))
SecondNumber = int(input("Введи второе число: "))

Result = int(0)

if Action == "+":
    Result = FirstNumber + SecondNumber
elif Action == "-":
    Result = FirstNumber - SecondNumber
elif Action == "*":
    Result = FirstNumber * SecondNumber
elif Action == "/":
    if SecondNumber == 0:
        print("Ошибка: деление на ноль!")
        exit()
    Result = FirstNumber / SecondNumber
else:
    print("Ошибка: неверный оператор!")
    exit()

print("Результат:", Result)

