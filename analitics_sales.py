import pandas as pd

with open('sales.csv', 'r', encoding='UTF-8') as file:
    data = pd.read_csv(file)

print('-------------\ntask 1\n-------------')
city_set = set(data['Регион'])
region_totalsales = dict()
for city in city_set:
    region_totalsales[city] = sum(data[data['Регион'] == city]['Сумма продаж'])
print('Регион с наибольшими продажами:', max(region_totalsales, key=region_totalsales.get))

print('-------------\ntask 2\n-------------')
product_set = set(data['Название товара'])
product_sales = dict()
for product in product_set:
    product_sales[product] = sum(data[data['Название товара'] == product]['Количество проданных единиц'])
print('Наиболее продоваемый товар:', max(product_sales, key=product_sales.get))

print('-------------\ntask 3\n-------------')
print(data.pivot_table(index=['Регион'], columns=['Название товара'], values=['Количество проданных единиц'],
                       aggfunc='sum'))

print('-------------\ntask 4\n-------------')  # average check
# первое решение
# average_check = region_totalsales.copy()
# city_set = set(data['Регион'])
# for city in city_set:
#     num_buyers = list(data['Регион']).count(city)
#     average_check[city] /= num_buyers
# for i in average_check:
#     print(i, average_check[i])

# второе решение более компактное
average_check = data.pivot_table(index=['Регион'], values=['Сумма продаж'],aggfunc='mean')
average_check = average_check.rename(columns={'Сумма продаж': 'Средний чек'})
print(average_check)