# # marks = int(input("enter your marks:"))
# # if marks >= 90:
# #     print("A grade")
# # # elif marks >= 80:
# # #     print("B grade")
# # # elif marks >= 70:
# # #     print("C grade")
# # # else:
# # #     print("fail")


# # a = []
# # for i in range(1,41):
# #     if (i%2!=0):
# #         a.append(i)

# # a=[i for i in range(1,41) if i%2!=0]
# # print(a)


# # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # f=[i for i in  fruits if len(i)>5]
# # print(f)

# # a = [1,2,3,4,5,6,7,8,9]
# # d =["even" if i%2==0 else "odd" for i in a]
# # print(d)

# # b= [1,2,3,4,5,6,7,8,9,9999]
# # e=["even" if i%2==0 else "odd" for i in b]
# # print(e)

# # n = ['harpreet', 'sandeep', 'manpreet', 'jaskaran', 'baljit', 'simran', 'jaspreet']
# # d = [i.upper() for i in n]
# # print (d)
# import math
# n = [6,9,10,12,25]
# d = [math.sqrt(i) for i in n]
# print (d)

# nn = [6,9,10,12,25]
# m = [i**0.5 for i in nn]
# print (m)


# nnx = [6,9,10,12,25]
# mm = [i**2 for i in nnx]
# print (mm)

# nnn = [6,9,10,12,25]
# o = [i*i for i in nnn]
# print (o)


# x = [1,2,3,4,5]
# y = [i if i%2==0 else i*10 for i in x]
# print(y)



# list comprehension
# a = [i*i for i in range (10) if i%2==0]
# print(a)

# b = ['even' if i%2==0 else 'odd' for i in range(20+1)]
# print(b)

# 2d dict
# d = {"name": {"first_name": "gaurav", "last_name": "singh"}, "age": 25, "address": {"temp" : "mohali", "permanent": "himachal"} }
# print (d['name']['first_name']) 

# d = {}
# for i in range (1,10+1):
#     d[i] = i**2
# print(d)

# d2 ={i : "even" if i%2==0 else "odd" for i in range(1,10+1)}
# print(d2)
