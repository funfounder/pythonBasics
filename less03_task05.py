#взял первое решение, добавил обработку ошибки ввода.

# def summ():
#     ex = False
#     final_result = 0
#     while ex == False:
#         try:
#             numbers = input('Insert numbers diveded with spaces or enter "Q" to quit: ').upper().split()
#             result = 0
#             for i in range(len(numbers)):
#                 if numbers[i] == 'Q':
#                     ex = True
#                     break
#                 else:
#                     result = result + int(numbers[i])
#             final_result = final_result + result
#         except ValueError:
#             print('You have entered string!')
#         print(f'Current sum is {final_result}')
#     print(f'Program finished! Final result is {final_result}')


#смотрю на это решение, так получается пользователя выкинет при вводе любого символа не числа. нужно подумать как реализовать проверку на именно такой ключ. подумаю.
def summ():
    result = 0
    try:
        while result != '-':
            for i in map(int, input('Insert numbers diveded with spaces or enter "-" to quit: ').split()):
                result += i
            print(f'Current sum is {result}')
    except ValueError:
        print(f'Program finished. The result: {result}')


summ()