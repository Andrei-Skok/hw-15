import json

#task 1
# dict_ = dict()
# while True:
#     item = input('Input item: ')
#     if item != 'stop':
#         price = input('Input price: ')
#         dict_[item] = float(price)
#     else:
#         break
# with open('shopping.json', 'w') as file:
#     json.dump(dict_, file)

#task 2
with open('shopping.json', 'r') as file:
    data = json.load(file)
    prices = list(data.values())
    for i in prices:
        print(i)
    print(f'total price for all = {sum(prices)}')