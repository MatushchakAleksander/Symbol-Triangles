# 4.Вывести треугольник  с шириной N с помощью цикла while

N = int(input('Enter a value for the width of the triangle: '))
counter = N
counter_2 = 0
while True:
    if 0 < counter <= N:
        counter = counter-1
        counter_2 = counter_2+1
        print(' '*counter+'*'*counter_2)
