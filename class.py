# click = True
# like = 0
# if click:
#     like = like + 1
#
# print(like)

# def max(a,b):
#     if a > b:
#         print('a is the max')
#     else:
#         print('b is the max')
#
# max(1,2)

# if (10<0) and (0 <=10):
#     print("A")
# else:
#     print("B")

# a = "b"
# if True or True:
#     a = "c"
# print(a * 2)

# for number in range(10):
#     if number % 3 == 1:
#         print(number)
#         print("Divisible by 3")
#         continue
#     print(number)
#     print("Not Divisible by 3")

# Word = "Hello"
# Letters = []
# for w in Word:
#     Letters.append(w)
# print(Letters)
#
# for user in range(10)

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i +=1

# counter = 1
# while len (counter <= 10):
#     print(counter)
#     counter = counter + 1

# Word = "Hello"
# Letters = []
# for W in Word:
#     Letters.append(W)
#
# print(Letters)

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 1

# counter = 1
# while ( counter <= 10 ):
#     print(counter)
#     counter = counter + 1
#
# X = 'abcd'
# for i in range(len(X)):
#    print(i)

# Length = 10
# for chr in range(1, Length+1):
# 	print("0"*chr)
#
# for chr in range(Length,0,-1):
# 	print("0"*chr)


#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4
# 12345

# for rows in range(5):
#     if rows % 2 == 0:
#         print(" | | ")
#     else:
#         print("-----")

# for rows in range(5):
#     if rows % 2 == 0:
#         for columns in range(1, 6):
#             if columns % 2 == 1:
#                 if columns != 5:
#                     print(" ", end="")
#                 else:
#                     print(" ")
#             else:
#                 print("|", end="")
#     else:
#         print("-----")

# Sets
country_list = []

for i in range(5):
    country = input("Please Enter Your Country:")
    country_list.append(country)

# set_country = set(country_list)
#
# print(country_list)
# print(set_country)

# Dictionary
country_directory = {}

for country in country_list:
    if country in country_directory:
        country_directory[country] += 1
    else:
        country_directory[country] = 1

print(country_directory)

