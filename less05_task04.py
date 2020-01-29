my_in = open('05_04.txt', 'r')
my_out = open('05_04_out.txt', 'w', encoding='utf-8')

my_dict = {}
for line in my_in:
    el = line.strip().split()
    key, value = el[0], el[1:]
    my_dict.setdefault(key, []).extend(value)

rus = ['Один','Два','Три','Четыре',]

dict_out = {}
i = 0
for key, value in my_dict.items():
    key = rus[i]
    dict_out[key] = value
    i += 1

my_list = []
for key, value in dict_out.items():
        line = key + ' ' + value[0] + ' ' + value[1]
        my_out.write(line)
        my_out.write('\n')

# print(my_list)
# print(my_dict)
# print(dict_out)
# print(dict_out['Один'])