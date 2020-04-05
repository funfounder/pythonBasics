from itertools import count
my_file = open('05_02.txt', 'r')

i = 1
for line in my_file:
        if line == '\n':
            line = line.rstrip('\n')
            print(f"Line {i} doesn't contain words")
            i +=1
        else:
            line = line.rstrip('\n')
            word_count = line.count(' ') + 1
            print(f'Line {i} contains {word_count} words')
            i += 1
print(f'File contains {i} lines totally.')
my_file.close()