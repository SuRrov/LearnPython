Number = int(input("Введи число: "))

if Number%3 == 0:
    print("Число делится на 3")

if Number >= 10:
    print("Число больше 10")

if Number%3 != 0 and Number < 10:
    print("Число не соответствует условиям")