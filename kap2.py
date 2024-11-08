import matplotlib.pyplot as plt

prices = {}
with open('products.txt', 'r', encoding='utf-8') as file:
    for line in file:
        product, price = line.strip().split(': ')
        prices[product] = float(price)

plt.bar(prices.keys(), prices.values(), color='blue')
plt.xlabel('Продукти') 
plt.ylabel('Ціна') 
plt.title('Ціни на продукти')  

plt.show()
