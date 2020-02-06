import json

with open('05_07_out.txt', 'w', encoding='utf-8') as json_file:
    with open('05_07.txt', encoding='utf-8') as my_file:
        subjects = {}
        interm = {}
        total_profit, comp_positive = 0, 0
        line = my_file.read().split('\n')
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                total_profit += profit
                comp_positive += 1
            interm['average_profit'] = total_profit / comp_positive
        total_list = [subjects, interm]
        json.dump(total_list, json_file, ensure_ascii=False, indent=4)

print(f'All information for firms: \n{line}\n\nTotal list: \n{total_list}')