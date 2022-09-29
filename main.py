'''
sides = [3, 2, 4, 7, 12, 11, 13, 15, 16, 14, 14]

sides = sorted(sides, reverse=True)

smax = 0
for i in range (len(sides)):
    for j in range(i+1, len(sides)):
        for k in range(j+1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a+b > c and a+c > b and b+c > a:
                p=(a+b+c)/2
                s=(p*(p-a)*(p-b)*(p-c))**(1/2)
                if s > smax:
                    smax = s

print('Максимальная площадь треугольника', smax)
'''
import math


print('a*x**2 + b*x + c')


a = int(input('Коэффициент a: '))
b = int(input('Коэффициент b: '))
c = int(input('Коэффициент c: '))

if a == 0:
    print('Невозможно решить')

d = b**2 - 4*a*c

print('Дискриминант равен: ', d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print('Корни уравнения: ', x1, ' ,', x2)

elif d == 0:
    x = -b / 2*a
    print('Корень уравнения: ', x)
elif d < 0:
    print('Нет решения')


