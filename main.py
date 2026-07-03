# 'a = int(input("Enter the 1st num:"))
# op = input("enter the ops:")
# b = int(input("enter the 2nd num:"))
# print("the result of the calc is:")
# if op == "+":
#      print(a+b)
# elif op == "-":
#      print(a-b)
# elif op == "*":
#      print(a*b)
# elif op == "/":
#      print(a/b)
# else:
#      print("operation is not valid")


# number = [10,20,30]

# print(20 in number)
# print (40 in number)


# text = "python"
# print ("y"in text) #true
# print("x" in text)  #false


# a =[1,2,3]
# b=a
# print(a is b)   #true
# print(a is not b) #false


# a = [1,2,3]
# b = [1,2,3]
# print(a is b)   #false
# a = int(input("Enter your age:"))
# if a >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


# print("Enter your age:")


# marks = int(input("enter your marks:"))
# if marks >= 90:
#     print("A grade")
# elif marks >= 80:
#     print("B grade")
# elif marks >= 70:
#     print("C grade")
# else: 
#     print("fail")
# for i in range(1,10,2):
# #     print(i)
# for i in range (10):
#     print("hello")


# input = int(input("Enter a number:"))
# if input % 5 == 0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")


# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# for i in range(7):
#     print("python")



# Program to swap values without using a third variable

# x = 10
# y = 25
# x = x + y   
# y = x - y   
# x = x - y  

# print("After swapping:")
# print("x =", x)
# print("y =", y)

#==========================================================================

# Program to check if a year is a leap year

# Ask the user for a year
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# FizzBuzz program from 1 to 20



# for num in range(1, 21):   # loop from 1 to 20
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Factorial program using for loop

# num = int(input("Enter a number: "))

# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i

# print("Factorial of " + str(num) +  " is "  + str(factorial))


# Discount System Program

# Take purchase amount as input
# amount = float(input("Enter purchase amount: "))
# # discount 
# if amount > 500:
#     discount = 0.20  
# elif amount > 100:
#     discount = 0.10   
# else:
#     discount = 0.0    
# final_amount = amount - (amount * discount)

# print("Final amount after discount is:", final_amount)


# Fibonacci Sequence Program

# # Take input from user
# n = int(input("Enter how many numbers to print: "))

# # First two numbers of Fibonacci sequence
# a, b = 0, 1

# print("Fibonacci sequence:")

# # Loop n times
# for i in range(n):
#     print(a, end=" ")   # print current number
#     a, b = b, a + b     # update values (next number = sum of previous two)



# # Star Pattern Program

# # Take number of rows from user
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()   # move to next line


# dictionary
#create a dictionary as number its keys and its
#  correspondings squares as its values upto 10 numbers only 

# d = {}
#     n = i**2 for i in range (1,11)
# print(n)

# names = ['neha','karan','nikita']
# d = {}
# for i in names:
# d[i] = len(i)


# d3 ={i:len(i) for in in names}
# print(d)

# # d = {even if i%=0 else odd}

# my method
# student={'sumit': 90, 'neha': 50, 'karan':40 , 'nikita': 92}
# for i,j in student.items():
#     if j >=50:
#         print(f"{i} -- {j} pass")
#     else:
#         print(f"{i} -- {j} fail")

# # teacher method

# students = {"Alice": 72, "Bob": 45, "Charlie": 88}

# d5 = {i: "pass" if students[i] > 50 else "fail" for i in students}
# print(d5)


# functions.py
# built in functions = map() , len() , print() , input() , type() , int() , str() , float() , list() , dict() , set() , tuple() , range() , sum() , max() , min() , sorted() , reversed() , enumerate() , zip() , filter() , any() , all()
# user defined functions = def function_name(parameters):  , return value
# return value = def function_name(parameters):  , return value


# def greet():
#     # print("Hello, welcome")
#     return "Hello, welcome"
# a=greet()
# print(a)

# def katable(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")

# katable(5)

# # prime or not
# def is_prime(n):
#     count = 0
#     for i in range(2,11):
#         if (n % i == 0):
#             count = 1
#             break
#     if count == 0:
#         return "prime"
#     else:
#         return "not prime"
# a=is_prime(117)
# print(a)

# sort and duplicates
# def remove_duplicates_and_sort(a):
#     a.sort()
#     i=0
#     while(i<len(a)):
#         if a[i]==a[i-1]:
#             del a[i-1]
        
#         i+=1
#     return a



# a = [1,91,1,2,2,2,3,3,3,4,4,4,5,5,5]
# print(remove_duplicates_and_sort(a))
# b = sorted(list(set(a)))
# print(b)

# o = {1:'odd' , 2:'even' , 3:'odd' , 4:'even' , 5:'odd' , 6:'even' , 7:'odd' , 8:'even' , 9:'odd' , 10:'even'}
# reverse = {i:j for j,i in o.items() }
# print(reverse)

# def sum(a,b):
#     return a+b

# def sum():
#     31a = int(input("Enter the 1st num:"))
#     b = int(input("Enter the 2nd num:"))
#     return a+b
# print(sum())

# positional arguments
# def multi(a,b,c,d):
#     return a*b*c*d

# print(multi(1,2,3,4))

#keyword argument
# def sub(a, b , c):
#     print(a-b-c)

# sub(a=10,c=56,b=2)

# default parameter
# def summ (a,b,c=0): # giving the default value if we have to bypass argument error on e element to add two values
#     return a+b+c
# print(summ(10,20,30))

# args
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(10,20,30,40,50,60))
# print(add(100,200,300,400,500,600,700,800,900,1000))
# # practice
# def summ(*a):
#     sum = 0 
#     for i in a:
#         sum += i
#         print(sum)
# summ(10,20,30,40,50,60)
# summ(100,200,300,400,500,600,700,800,900,1000)


#kwargs
# def kwargs(**k):
#     for i,j in k.items():
#         print(f"{i} : {j}")

# kwargs(name="neha" , age=20 , city="delhi")
# print(kwargs(name="neha" , age=20 , city="delhi"))


#special functions

# double = lambda x : x*2
# print(double(4))
# # add
# add = lambda a,b,c : a+b+c
# print(add(5,5,5))

# # check
# check = lambda a: "even" if a%2==0 else "odd"
# print(check(5))

# 2. map function
# li = ['1','2','3','4']
# convert = map(int,li)
# print(list(convert))
# print(tuple(convert))

# def square(x):
#     return x * x
# t1 = (1,2,3,4)
# square1 = map(square ,t1)
# print(list(square1))

# filter function
# def age(a):
#     if a >= 18:
#         return True
#     else:
#         return False
# li1 = [12, 18, 20, 15, 25, 30]
# li2 = filter(age,li1)
# print(list(li2))
# check1 = filter(lambda x : True if x >= 18 else False , li1)
# check2 = filter(lambda x : True if x >= 18 else False , li2)
# print(list(check1))
# print(list(check2))

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(list(enumerate(fruits)))

# for i in enumerate(fruits):
#     print(i)

# for i,j in enumerate(fruits,start=1):
#     print(i,j)

# with open("file.txt","w") as file:
#     file.write("nono\n")
#     file.write("neha\n")
#     print("file created successfully")

# with open("file.txt","r") as file:
#     contents = file.read()
#     print(contents)

# with open("file.txt","w") as file:
#     file.write("motu\n")
#     print("file appended successfully")

# with open("file.txt","r") as file:
#     for line in file:
#         print("student:{}".format(line.strip()))

# with open("file.txt","r") as file:
#     lines_list = file.readlines()
#     print(lines_list)
#     print("Total lines in the file:", len(lines_list))

import os
print(os.path.exists("file.txt"))

