# 3.Вывести треугольник  с шириной N с помощью цикла while

N = int(input('Enter a value for the width of the triangle: '))
counter = N        
counter_1 = -1
while True:
    if 0 < counter <= N:
        counter = counter-1
        counter_1 = counter_1+1
        print(' '*counter_1+'*'*counter+'*')
