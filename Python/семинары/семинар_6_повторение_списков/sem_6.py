'''39.Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут
в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в
первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
Затем элементы второго массива'''

# list1 = [int(input("1: ")) for i in range(int(input("первый массив: ")))]

# list2 = [int(input("2: ")) for i in range(int(input("второй массив: ")))]
# print(list1)
# print(list2)

# # for i in list1:
# #     if i not in list2:
# #         print(i, end=" ")

# # или
# list3 = [i for i in list1 if i not in list2]
# print(*list3)

'''Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.'''

# list1 = [int(input("элементы: ")) for i in range(int(input("количество элементов: ")))]

# count =0
# for i in range(1, len(list1)-1):
    
#     if list1[i]> list1[i-1] and list1[i]> list1[i+1]: #или list1[i-1]< list1[i] > list1[i+1]
#         count+=1
# print("ответ",count)



'''43.Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.'''


# list2 = [int(i) for i in input(":").split()]

# count = 0
# for i in range(len(list2)):
#     for j in range(i+1, len(list2)):
#         if list2[i] == list2[j]:
#             count+=1
# print(count)

'''Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).'''

k = int(input(":"))
list1 = []
for i in range(k):
    temp_sum =0
    for j in range(1, i//2+1):
        if i %j == 0:
            temp_sum+= j
    list1.append(tuple([i, temp_sum]))

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if (i!=j) and list1[i][0]== list1[j][1] and(list1[i][1] == list1[j][0]):
            print(*list1[i])
    

