##  A list of product prices in dolars

dollar_prices = [10.5, 20.0, 15.75, 30.0, 25.5]
cents_prices = []
for price in dollar_prices:
    cents_price = price * 100
    cents_prices.append(cents_price)
print(cents_prices)