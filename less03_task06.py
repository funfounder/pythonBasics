def my_func():
    word = input('Insert a line devided with spaces: ')
    char, result = [], []
    if len(word) > 0:
        for i in word.split():
            char.append(i[0].upper() + i[1:])
        result = ' '.join(char)
    return print(result)


my_func()


#lamba чтобы разобраться как это работает.
#но тогда пропадает формат. можно как-то сохранить формат при использовании ламба?
#
# my_func = lambda words: print(words.title())
#
# my_func(input('Insert the line: '))






