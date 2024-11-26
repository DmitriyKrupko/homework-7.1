x = input('Введите целое число: ')
while not x.isdigit():
    print("Ошибка")
    x = input('Введите целое число: ')
for y in range(10):
        z = x.count(str(y))
        if z:
            print("Цифр", y, "в числе", z)
