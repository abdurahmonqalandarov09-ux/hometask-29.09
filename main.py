# def show_arguments(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs)
#     return inner

# @show_arguments
# def multiply(a, b):
#     return a * b

# a = int(input())
# b = int(input())

# print("Functions:", a, b)
# print(multiply(a, b))



# test 2

# def frame(func):
#     def inner(*args, **kwargs):
#         print("=" * 10)
#         t = func(*args, **kwargs)
#         print(t)
#         print("=" * 10)
#         return func
#     return inner

# @frame
# def show_text(text):
#     return text

# a = input()
# print(show_text(a))



# test 3

# def double_result(func):
#     def inner(num):
#         return func(num + num)
#     return inner


# @double_result
# def get_number(number):
#     return number

# n = int(input())
# print(get_number(n))


# test 4

# multiply = lambda a, b: a * b

# num1 = int(input())
# num2 = int(input())

# print(multiply(num1, num2))


# test 5

# def count_calls(repeat):
#     def inner(func):
#         def inner1(*args, **kwargs):
#             cnt = 0
#             for i in range (repeat):
#                 cnt+=1
#                 func(*args, **kwargs)
#                 print("Call:", cnt)
#         return inner1
#     return inner

# @count_calls(3)
# def hello():
#     print("Hello")


# hello()


# test 6

# def string_only(func):
#     def inner(value):
#         if isinstance(value, str):
#             return func(value)
#         else:
#             print("A string is required")
#     return inner

# @string_only
# def show(value):
#     return value

# a = input()


# try:
#     value = int(a)
# except ValueError:
#     value = a
    

# print(show(value))


# test 7


# def adults_only(func):
#     def inner(age):
#         if age >= 18:
#             print("Welcome!")
#         else:
#             print("Access denied")
#     return inner

# @adults_only
# def enter_club(age):
#     return age

# a = int(input())

# print(enter_club(a))

# test 9

# def add_prefix(func):
#     def inner(name):
#         return f"Result: {name}"
#     return inner

# @add_prefix
# def get_name(name):
#     return name

# a = input()
# print(get_name(a))


# test 10

# def check_division(func):
#     def inner(a, b):
#         if a == 0 or b == 0:
#             print("Cannot divide by zero")
#         else:
#             return func(a, b)
#     return inner

# @check_division
# def divide(a, b):
#     return a / b

# num = int(input())
# num1 = int(input())

# print(divide(num, num1))


# test 11

# numbers = list(map(int,input().split()))
# p = list(filter(lambda x: x > 0, numbers))

# print(p)