dream_cars = ['golf','lambo','porshe','lada','patrol']
cars_prices = [500000, 3000000, 320000, 280000, 130000]
for i,car in enumerate(dream_cars,1):
    print(f'{i} {car.title()}')
#NEW PRICES WITH LIST COMPREHENSION
price_sell = [int(price * 0.85) for price in cars_prices ]
print('This is the price with 15% sales:')
for i,price in enumerate(price_sell,1):
    print(f"{i}.{dream_cars[i-1]} : {price_sell[i-1]}")
