"""Задача 8: 
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no"""

a = int(input("Введите первое число: ")) 
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a*b>c and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")