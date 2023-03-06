#Задача №28
a = int(input("введите число 1 "))
b = int(input("введите число 2 "))


def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)


print(sum(a, b))