start = int(input('Insert the starting range: '))
goal = int(input('Insert the goal range: '))

i = 0
progress = 0

while progress < goal:
    if i == 0:
        progress = start * 1.1
        i += 1
    else:
        progress = progress * 1.1
        i += 1
print(f'You will achieve your goal in {i + 1} day(s)')
