"""По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while


Input: 5

Output: 120"""


# n = int(input())
# i = 1
# res = 1
# while i<=n:
#     res = res*i
#     i = i+1
# print(res)


"""11. 
Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи,выведите число -1.

Input: 5
Output: 6"""

# 1 2 3 4 5 6 7  8  9
# 0 1 1 2 3 5 8 13 21

# n = int(input())
# x = 0
# n1 = 0
# n2 = 1
# i = 2
# while x < n:
#     x = n1 +n2
#     n1 = n2
#     n2 = x
#     i = i+1
#     if(x > n):
#         i = -1
# print(i)

"""Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая
длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те,
в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько
дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная
температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих
строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий
день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2"""

# n = int(input())
# k = 0
# max = 0
# for i in range(n) :
#     x = int(input())
#     if x >0:
#         k = k+1
#     else:
#         max = k
#         k = 0
#     if max < k:
#         max = k
# print(max)


"""# 15. 
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 3000
# Input: 5 -> 5 1 6 5 9
# Output: 1 9"""


# n = int(input("кол-во арбузов: "))
# x = int(input("вес 1 арб: "))
# max = x
# min = x
# for i in range(n-1) :
#     x = int(input("")) 
#     if x> max: 
#         max = x
#     if x < min:
#         min = x
# print("max = ", max, "min = ", min)

# или


# n = int(input("кол-во арбузов: "))
# max = -1
# min = 3001
# for i in range(n) :
#     x = int(input("")) 
#     if x> max: 
#         max = x
#     if x < min:
#         min = x
# print("max = ", max, "min = ", min)
