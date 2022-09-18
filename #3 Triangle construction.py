# 3.Вывести треугольник  с шириной N с помощью цикла while

a = int(input('Enter a value for the width of the triangle: '))
counter = a        
counter_1 = -1
while True:
    if 0 < counter <= a:
        counter = counter-1
        counter_1 = counter_1+1
        print(' '*counter_1+'*'*counter+'*')
