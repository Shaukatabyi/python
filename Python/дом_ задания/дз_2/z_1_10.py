"""Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
2"""

n = int(input())
n0 = 0
n1 = 0
for i in range(n) :
    x = int(input())
    if x == 1:
        n1=n1+1
    elif x == 0:
        n0 = n0+1
if n0 < n1:
    print(n0)
else:
    print(n1)  