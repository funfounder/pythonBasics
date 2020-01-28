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

def fibo_gen(n):
    m = 1
    for i in range(1, n):
        if i > 15:
            break
        m *= i
        yield m

for i in fibo_gen(26):
    print(i)