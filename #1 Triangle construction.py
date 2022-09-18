# 1.Вывести треугольник  с шириной N с помощью цикла while

a = int(input('Enter a value for the width of the triangle: '))
counter = a        

while True:
    if 0 < counter <= a:
        counter = counter-1
        res = ('*'*counter+'*')
        print(res)
