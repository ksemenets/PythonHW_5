#Задача №26
a = int(input("введите число"))
b = int(input("в какую степень возведем?"))


def pow(a, b):
    if b == 1:
        return a
    return a * pow(a, b-1)


print(pow(a, b))