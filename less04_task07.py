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
    n = int(input('Insert positive number: '))
    m = 1
    global num
    for num in range(1, n):
        m *= num
        yield m

for i in fibo_gen():
    if num <15:
        print(f'Factorial {num} = {i}')
    else:
        print()