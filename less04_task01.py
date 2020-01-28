from sys import argv

script_name, hours, rate, bonus = argv

if int(bonus) <= 0:
    print('You have entered 0 bonus!')
try:
    result = (int(hours) * int(rate)) + int(bonus)
    print(f'Total salary is {result}')
except ValueError:
    print('Only integers are allowed!')