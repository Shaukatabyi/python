'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
4 -> 1 2 3 4
9

5 -> 9 1 1 4 9
22'''

# n = int(input("кол-во кустов в грядке: "))
# list1 = []
# for i in range(n):
#     list1.append(int(input("кол-во ягод в кусте: ")))
# print(list1)
# max1 = list1[-1] + list1[0] + list1[1]

# for j in range(len(list1)-1):
#     max2 = list1[j-1] + list1[j] + list1[j+1]
#     if max2 >max1:
#         max1 = max2
#     max3 = (list1[-2] + list1[-1] + list1[0])
#     if (max3)> max1:
#         max1=(max3)
# print(max1)

# или

n = int(input("кол-во кустов в грядке: "))
B = [int(input("кол-во ягод в кусте: ")) for i in range(n)]
print(B)

sum = 0

B = B+B[:2]
print(B)

for i in range(n):
    sum = max(sum, B[i] + B[i+1] + B[i+2])
print(sum)