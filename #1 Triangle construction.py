# 1.Вывести треугольник  с шириной N с помощью цикла while

N = int(input('Enter a value for the width of the triangle: '))
counter = N        

while True:
    if 0 < counter <= N:
        counter = counter-1
        res = ('*'*counter+'*')
        print(res)
