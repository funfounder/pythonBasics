from math import factorial

def fact():
    global n
    n = int(input('Input number: '))
    yield factorial(n)

f = fact()
print(f)

# my_list = [i for i in range(fact())]
# print(my_list)

# c = 0
# for el in fact(n):
#     if c < n:
#         print(el)
#         c +=1
#     else:
#         break