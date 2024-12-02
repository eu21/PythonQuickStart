# Task 1

# n = input("Choose a number between 0 and 10 and enter it here: ")
# if int(n) > 10:
#     print("Your number is greater than 10")
# else:
#     print("Your number was checked and number is correct and number is: "+n)


# Task 2

# def minimum(x ,y):
#     if x < y:
#         return x
#     else:
#         return y

# x = input("Assign a number to x here: ")
# y = input("Assign a number to y here: ")

# print("The smaller number is: " + minimum(x ,y))


# Task 3 (elif statements)

# raining = input("Is it raining? (yes/no): ")
# haveUmbrella = input("Have umbrella? (yes/no): ")
# if raining =="yes" and haveUmbrella == "yes":
#     print("Bad weather, but you are smart!")
# elif raining =="yes" and haveUmbrella == "no":
#     print("Put on waterproof jacket!")
# elif raining =="no" and haveUmbrella == "no":
#     print("It is nice weather!")


# Task 4

# def absulute_val(num):
#     if num < 0:
#         return -1 * num
#     elif num == 0:
#         return 0
#     else:
#         return num

# result = absulute_val(-6)
# print(result) #6
 
# result = absulute_val(6)
# print(result) #6
 
# result = absulute_val(0)
# print(result) #0 

# result = absulute_val(45.6)
# print(result) #45.6

# # Task 5
# word = "serendipitous"
# vouwels = ("a", "e", "i", "o", "u")
# vowelCount = 0

# for character in word:
#     if character in vouwels:
#         vowelCount += 1
        
# print(vowelCount+1)


#Task 6 (Ranges)

# for i in "mother":
#     print(i)
# Output:
# m
# o
# t
# h
# e
# r

# for i in range(4):
#     print(i)
# 0
# 1
# 2
# 3

# range(1,8,3) from 1 to 8 with step 3
# for i in range(1,8,3):
#     print(i)
# 1
# 4
# 7


# for i in range(2, 8, 2):
#     print(i)

# Range(start(inclusive), stop(exlusive),step)

# for i in range(23, 101):
#     print(i)

# i=0
# while i<1000:
#     i+=1
#     print(i)


vouwels = ("a", "e", "i", "o", "u")

# iterate tuple with for loop
# for ch in vouwels:
#     print(ch)

#same with while loop
# index=0
# while index<len(vouwels): #index must be less than length of vouwels sequence
#     print(vouwels[index])
#     index+=1
