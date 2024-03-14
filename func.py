# def amaan():
#     a=10       #local variable
#     print(a)
# b=19            #global variable
# amaan()
# print(b)

# def fun3(a,b): #positional arguments
#     print(a,b)
# func3(2,3)

# def fun10(a,b=20): #default arguments
#     print(a,b)
# func4(29)

# def fun11(a,b): #keyword arguments
#     print(a,b)
# func4(a=29,b=30)

# def fun12(*args): #arbitary arguments
#     for i in args:
#         print(i)
# func4(29,20,30)

# def max(a,b):  #returning max 
#     if(a>b):
#         return a
#     else:
#         return b
# a=max(10,22)
# print(a)



       #map reduce filter      
                                                       

# from functools import reduce
# my_list=[1,2,3,4,5,6,7,8,9,10]
# new_list=list(filter(lambda x:(x%3==0),my_list))
# print(new_list)

# new_list=list(map(lambda x: x*5,my_list))
# print(new_list)

# new=reduce(lambda x,y:x*y,my_list)
# print(new)


# even=list(filter(lambda x:x%2==0,my_list))
# print(even)
# odd=list(filter(lambda x:x%2!=0,my_list))
# print(odd)
# square=list(map(lambda x:x*x,my_list))
# print(square)


list1=[1,2,3]
list2=[4,5,6]
list3=[]
new_list=list(map(lambda x,y:x+y,list1 ,list2))
print(new_list)

# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(8))



# add=list(map(lambda x:list3.append(x),list1))
# add=list(map(lambda x:list3.up))
# list3 = list(map(lambda x, y: x + y, list1, list2))
# print(list3)



