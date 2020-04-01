products = []
param = {'name': '', 'price': '', 'quantity': '', 'units': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'units': []}
i = 0
while True:
    if input('To exit insert Q, to continue press Enter: ').upper() == 'Q':
        break
    i += 1
    print(f'Library of the parameters: {param}')
    for p in param.keys():
        prod_param = input(f'Insert the feature "{p}": ')
        param[p] = int(prod_param) if (p == 'price' or p == 'quantity') else prod_param
        analytics[p].append(param[p])
    products.append((i, param))
    print(f'\n Current list of products:')
    for product in products:
        print(product)
    print(f'\n Analytics of products:')
    for key, value in analytics.items():
        print(f'{key}:{value}')