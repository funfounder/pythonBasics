mydict = {}
with open('05_06.txt', encoding='utf-8') as my_file:
    for el in my_file:
        name, stats = el.split(':')
        n_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mydict[name] = n_sum
print(f'{mydict}')