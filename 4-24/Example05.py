#-*- coding:utf-8 -*-

# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
# #输出第10个斐波那契数列
# print(fib(10))


#递归
def fib(n):
    if n ==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
#输出第10个斐波那契数列
print(fib(10))




