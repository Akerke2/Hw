# 1
# a = 1
# b = 10
# c = int(input("шаг"))
# for i in range(a,b+1,c):
#     print(i, end=" ")

# # 2

# n = int(input("N"))
# sum = 0
# for i in range(n):
#     x = int(input("x"))
#     sum += x 
# print(sum)

# # 3

# x = []
# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i)

# # 4

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, "*", j, "=", i * j)

# # 5

# import time

# def countontdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = "{:02d}: {:02d}".format
#         (mins, secs)
#         print(timeformat, end = "\r")
#         time.slepp(1)
#     print ("Таймер завершён")
# countontdown(10)
# print("Finish!")



#  NEW сабақ
# FOR - ДЛЯ
# IN - В
# RANGE -  сандар АРАЛЫғы
# ИТЕРАЦИЯ - тізбектегі әрбір элементке кодты қолдану жеке жеке шығады
# += қосу


# d = ["hi", "hello", "hey"]
# for i in d:
#     print(i)

    # бірінші итерацияда hi
    # 2 - итерацияда hello
    # 3-ші итерацияда hey


# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print("sum of : ", total)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 4 == 0:
#         print(num, " is even")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
        # print(num" is even")


# text = "hello, world!"
# for i in text:
#     print(i+i) #екі рет шығады


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 2
# for num in numbers:
#     print(num*2)

# count = 1
# while count <= 5:  #-тен сан үлкен болмайынша цикл тоқтамайды
#     print(count)
#     count += 1    #


# count = 5
# while count >= 1:
#     print(count)
#     count -= 1


# count = 10
# while count <= 50:
#     print(count)
#     count += 1  


# count = 200
# while count >- 100:
#     print(count)
#     count -= 1



# count = 1
# total = 0

# while count >= 10:
#     total += count
#     count += 1
# print(total)


# hw
# 1
# user = input("Please enter your name: ")
# user_length = len(user)
# for string_index in range(user_length - 1, -1, -1):
#     character = user[string_index]
#     print(character)

# # 2
# def pcheck(word: str): 
#     iters = len(word)//2
#     for i in range(iters):
#         if word[i] != word[-i - 1]: 
#             return False 
#     return True 

# while True:
#     word = input('Enter a word: ')
#     print(f'{word} is palindrome' if pcheck() else 'not a palindrome') 

# 3
# firstList = [1,2,3]
# secondList=[]

# counter = len(firstList)-1

# while counter >= 0:
#     secondList.append(firstList[counter])
#     counter -= 1


# 4
# def largest_element(arr):
#     largest = arr[0]
#     for num in arr:
#         if num > largest:
#             largest = num
#     return largest



# While

# word = "almaty"
# e_word = ""
# for c in word:
#     e_word = c + e_word
# print(e_word)

    
# c жеке жеке әріп болып отырады

# city = ["Almaty", "Astana", "Karaganda"]
# fovcity = []
# for i in city:
#     fovcity = [i] + fovcity
# print(fovcity)


# и деген сити ішіндегі бөлек бөлек элемент
# и ді фовсити деген босмассивтің алдына қоятын болсақ ол сити деген массивті кері шығарады

# number = [5, 8, 6, 10, 9]
# max_number = [0]

# for number in number:
#     print(f"max_number({max_number}) < number({number})?")
#     if max_number < number:

# numbers = [3, 4, 1, 8, 2]
# max_number = numbers[0]
# i = 1
# while i < len(numbers):
#     if max_number < numbers[i]
#     max_number = numbers[i]
#     i += 1
# print(max_number) 


# # hw1

# list = []
# for i in range (1, 101):           
#     if i % 3 == 0 and i % 5 == 0:
#         list.append("FizzBuzz")
#     elif i % 3 == 0:
#         list.append("Fizz")
#     elif i % 5 == 0:
#         list.append("Buzz")
#     else:
#         list.append(i)
# print(list)

# for x in range(1, 101):
# if x % 3 == 0 and x % 5 == 0:
#     print("FizzBuzz")
# elif x % 3 == 0:
#     print("Fizz")
# elif x % 5 == 0:
#     print("Buzz")
# else:
#     print(x)



# 19.10.23
# total = 0
# for i in range(1, 31):
#     total = total + i
# print(total)
   
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1

# num = 10
# while num <= 1:
#     print(num)
#     num -= 1

# total = 0
# count = 10
# while count >= 1:
#     total += count
#     count -= 1
# print(total)


# count = 1
# while count <= 30:
#     if count % 2 == 0:
#         print(count)
#     count += 1

# total = 0
# count = 1
# while count <= 30:
#     if count % 2 == 1:
#         total += count
#     count += 1
# print(total)

# count = 1
# while count <= 30:
#     if count % 2 == 1:
#         count += 1
#         continue
#     print(count)
#     count += 1


# for i in range(1, 30):
#     if i == 10:
#         break
#     print(i)

# total = 0
# count = 50
# while count <= 100:
#     if count % 2 == 1:
#         total += 1
#         count += 1
# print(total)
    
# total = 0
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         total += 1
#     count += 1
# print(total)


#  hw1
# a = 10
# while a < 21:
#     print(a)
#     a = a ** a

# for i in range(10, 21):
#     print(i**2)

# 2
# a = 1
# n = int(input("enter num"))
# while n > a:
#     print(a)
#     a = a + 1
# print("num is num", n)

# 3
# a = 1
# n = int(input("num"))
# while n > a:
#     print(a * n)
#     a = a + 1

# 4

# for i in range(20, 51):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)

# 5
# for i in range (35, 88):
#     if i % 7 == 1 or 2 or 3:
#         print(i)
        
# 6 
# for i in range (1, 50):
#     if i % 5 == 0 or i % 7 ==0:
#         print(i)

# 7
# for i in range (10, 100):
#     if i % 4 == 0 and i % 6 != 0:
#         print(i)

# 8
# for i in range (10, 100):
#     if i % 2 != 0:
#         print(i)

# 9
# for i in range(100, 201):
#     if i % 17 == 0:
#         print(i)

# 10
# # k = 0
# a = 1 
# n = int(input("nummm"))
# while n > a:
#     if a % 2 == 0:
#     #  k += 1
#         print(a)



# 11
# n = int(input("hola"))
# a = 0
# for i in range (1, n+1):
#     a += i ** 2
# print("Сумма квадратов чисел от 1 до", n, "равна", a)