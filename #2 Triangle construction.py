# 2.Вывести треугольник  с шириной N с помощью цикла while

a = int(input('Enter a value for the width of the triangle: '))
counter = 0        

while True:
    if 0 <= counter <= a-1:
        counter = counter+1
        res = ('*'*counter)
        print(res)
