user_string = input('Insert a phrase: ')
task_list = list(user_string.split())
for ind, el in enumerate(task_list, 1):
    word_count = list(el)
    if len(word_count) <= 9:
        print(ind, el)
    else:
        print(ind, ''.join(word_count[:9]))