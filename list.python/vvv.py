# import random 
# random_list = random.sample(range(50), 1)
# print(random_list)
# filtered_random_list = []
# for random in random_list:
#     if len(random) > 5:
#        filtered_random_list.append(random)
# print(filtered_random_list)

# import random
# list =  random.sample(range(50), 6)
# print(list) 
# user = int(input("Enter any number: "))
# for i in range(user):
#     new_element = int(input("numbers"))
#     a.append(new_element)
#     print(a)

# # # 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# doubled_numbers = []
# for number in numbers:
#     doubled_numbers.append(number*2)
# print(doubled_numbers)
# print(sum(numbers))
# sum = 0

# Қосымша

# a = 5
# b = 2
# c = a * b
# d = a - b
# s = a // b
# g = a / b
# print(c, d, s, g)

# age = int(input("your age: "))
# if age > 18:
#     if age > 21:
# else: print ("Вы не можете голосовать")


# a = int(input("Age"))
# b = int(input("Height"))
# if a < b:
#     print(b - a)
# elif a > b:
#     print(a - b)
# elif a == b:
#     print(a + b)

# break деген токтату
# сountinue тастап кету, ары қарай жалғастыру
# a = 5
# b = 2
# c = input("tanba: ")
# if c =="*":
#     print(a * b)
# elif c =="/":
#     print(a / b)

# a = 1
# b = 5
# while a < b:
#     a = a + 1
#     if a == 3:
#         continue #Жалғастыру
#     print(a)

# while True:
#     c =input("san engiz: ")
#     if c=="0":
#         break

# a = 83
# v = 4
# l = 127
# f = 45
# j = ((a%v)+l)//f
# print(j)

# print(237**7( % 35) + 789 // 98)

# g = 567
# f = 127
# d = 84 
# e = 92
# print((g - f)**d % e)

# a = 237
# k = 7
# o = 35
# p = 789 
# d = 98
# l = ((237**7)%35+789)//98
# print(l)

# a = int(input("a"))
# b = int(input("b"))
# s = a * b
# print(s)

# c = float(input("c engiz"))
# f = c * 5/9 + 32
# print(f)

# a = int(input("a"))
# b = int(input("b"))
# m = int(input("m"))
# h = a + b + m
# d = h / 3
# print(d)

# a = int(input("a"))
# b = int(input("b"))
# if a > b:
#     print("true")
# elif b >= a:
#     print("False")

# b = int(input("b"))
# if b % 2:
#     print("number is odd")
# elif b > 0:
#     print("number is even")


# e = int(input("engiz"))
# if e <= 59:
#     print("Sizdin sanduk baganuz aryptik baganiz F")
# elif e <= 69:
#     print("Sizdin sanduk baganuz aryptik baganiz D")
# if e <= 79:
#     print("Sizdin sanduk baganuz aryptik baganiz C")
# elif e <= 89:
#     print("Sizdin sanduk baganuz aryptik baganiz B")
# if e <= 90:
#     print("Sizdin sanduk baganuz aryptik baganiz A")
# elif e <= 100:
#     print("Sizdin sanduk baganuz aryptik baganiz A")





# КОД КРАСНЫЙ

# thislist = ["apple", "cherry", "banana"] # Өзіңе керек элементті аласың. индекспен есептейді
# print(thislist[1])

# thslist = ["Almaty", "Astana", "Pavlodar"]  # элемент қосу соңынан қосады
# thslist.append("Karaganda")
# print(thslist)

# frukt = ["apple", "ananas", "banana"] # index  бойынша қосу 0-ден бастап санаймыз 0,1,2,3...
# frukt.insert(1, "dragonfrukt")
# print(frukt)


# thislist = ["apple", "watermelon", "banana"] # Бір элементтің орнына басқа сөз жазу керек болса
# thislist[0:2] = ["painapple", "ananas"]
# print(thislist)

# thislist = ["apple", "banana", "watermelon"] # Бир элементтин атын жазу аркылы удалить етемыз ("banana")
# thislist.remove("banana")
# print(thislist)

# thislist = ["Almaty", "Astana", "Karaganda"] # Элементтер бірінің астынан бірі тігінен тұру үшін
# for x in thislist:
#     print(x)


# thislist = ["Almaty", "Karaganda", "Astana", "Karaganda"] # Алфавить және цифрлар бойынша рет-ретімен қояды ABCD
# thislist.sort()
# print(thislist)

# thislist = ["Karaganda", "Almaty", "Astana"] # list1 i list2 бір-біріне ссылаться етып отырады сол үшін списокты коптровать ету үшін керек
# mylist = thislist.copy()
# print(mylist)

# list1 = ["Karaganda", "Almaty", "Astana"] # ЕКі бөлек списокты бір-біріне қосу үшін
# list2 = [1, 2, 3, 4]
# list3 = list1 + list2
# print(list3)

# thislist = ["Karaganda", "Almaty", "Astana"] # Элемент қосу индекс арқылы айнымалының жанына жазамыз индексті
# thislist[1] = "blackcurrant"
# print(thislist)
    
