from sys import argv
from itertools import count, cycle

script_name, start, circum = argv

my_list = []
for i in count(int(start)):
    if i < 15:
        my_list.append(i)
    else:
        break

print(my_list)

i = 0
my_cycle = []
for el in cycle(my_list):
    if i < int(circum):
        my_cycle.append(el)
        i +=1
    else:
        print(my_cycle)
        break