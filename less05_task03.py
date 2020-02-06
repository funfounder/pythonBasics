my_file = open('05_03.txt', 'r')

my_dict = {}
for line in my_file:
    key, value = line.split()
    my_dict[key] = value

total_budget = 0
count_emploe = 0
emp_low = []
emp_high = []

for key, value in my_dict.items():
    if float(value) < 20000:
        emp_low.append(key)
        total_budget += float(value)
        count_emploe +=1
    else:
        emp_high.append(key)
        total_budget += float(value)
        count_emploe += 1

print(f'The emploes with salary below 20k: {emp_low}.')
print(f'The emploes with salary above 20k: {emp_high}.')
print(f'Average salary is {(total_budget/count_emploe):.2f}')

my_file.close()