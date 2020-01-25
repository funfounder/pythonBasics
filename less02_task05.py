#совместил несколько решений

orig_list = [7, 5, 3, 3, 2]

q = None
while q != 'q':
    print(f'Current rating: {orig_list}')
    user_number = input('Insert rating number or Q to finish: ').upper()
    if user_number == 'Q':
        break
    else:
        user_number = int(user_number)
        if user_number < 1:
            print('Rating must be above zero!')
        else:
            i = 0
            for rating in orig_list:
                if user_number > rating:
                    break
                i += 1
            orig_list.insert(i, float(user_number))
            print(orig_list)
