user_list = input('Insert numbers splitted with spaces: ').split()
new_list = list(user_list) #создает копию, функцию использовать нельзя, а если поставить равно без какой-либо операции, то перезаписывает исходный лист
# for i in range(1, len(new_list), 2):
#     new_list[i-1], new_list[i] = new_list[i], new_list[i-1]
i = 0
while i+1 <len(user_list):
    if i % 2 == 0:
        new_list.insert(i, new_list.pop(i + 1))
    i +=1
print(f'Your list was {user_list}')
print(f'New list is {new_list}')
# для себя. в if - работаем с одним аргументом, просто получается, что pop откусывает четный и сдвигает его влево. он был i+1, а стал i. а i-тый элемент автоматически сдвигается влево.