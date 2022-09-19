# 2.Вывести треугольник  с шириной N с помощью цикла while

N = int(input('Enter a value for the width of the triangle: '))
counter = 0        

while True:
    if 0 <= counter <= N-1:
        counter = counter+1
                print('*'*counter)
