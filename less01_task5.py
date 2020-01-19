revenue = int(input('Enter revenue: '))
costs = int(input('Enter costs: '))

if revenue > costs:
    print('You have profit!')
    profit = revenue - costs
    cost_eff = profit / costs
    print(f'Your profitability is {cost_eff:.2f}')
    staff = int(input('How many people work for you: '))
    cost_empl = profit / staff
    print(f'Your cost-effectiveness per emploee is {cost_empl:.2f} ')
else:
    print('You have loss')
