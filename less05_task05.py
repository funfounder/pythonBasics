from random import  randint

sum_el = 0
with open('05_05.txt', 'w') as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + ' ')

print(f'Sum of elements = {sum_el}')