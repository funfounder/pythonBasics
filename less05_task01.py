my_file = open('kalinichenko.txt', 'w')

lines = []
while True:
    l = input('Please insert the elements. For end insert empty space " ": ')
    if l != ' ':
        lines.append(l + '\n')
    else:
        my_file.writelines(lines)
        print('Input is finished. Open the file.')
        break

my_file.close()