from math import factorial

# def fact():
#     global n
#     n = int(input('Input number: '))
#     yield factorial(n)
#
# f = fact()
#
# for i in f:
#     print(i)

# c = 0
# for el in fact(n):
#     if c < n:
#         print(el)
#         c +=1
#     else:
#         break

def fibo_gen():
    global num, user_num
    n = int(input('Insert positive number: '))
    m = 1
    user_num = factorial(n + 1)
    for num in range(1, n + 1):
        m *= num
        yield m

for i in fibo_gen():
    if num <= 15:
        print(f'Factorial {num} = {i}')
    else:
        print(f'\rCustom factorial of {num} = {user_num}', end='')