#TRTING TO LEARN ENUMORATE AND ALL OF THAT BELOW

foods = ['burger', 'pizza', 'sushi', 'kebab', 'pasta']
prices = [12, 18, 35, 10, 22]
for i,food in enumerate(foods,1):
    print(f"{i}.{food.title()}")

print("This will be the prices with discount!")

new_prices = [int(price * 0.75) for price in prices]
for i,price in enumerate(new_prices,1):
    print(f"{i}.{foods[i-1].title()} - {new_prices[i-1]}")

#NEX EXERCISE
drinks = ['cola', 'fanta', 'beer', 'water', 'rakia']
prices = [3, 3, 5, 2, 12]

for i, drink in enumerate(drinks, 1):
    print(f"{i}. {drink.title()}")

new_prices = [int(price * 0.70) for price in prices]

print("\nyou are saving:")
for i, price in enumerate(new_prices, 1):
    saved = prices[i-1] - price
    print(f"{i}. {drinks[i-1].title()} → you are saving {saved} lv")


#NEX EXERCISE
games = ['gta6', 'fifa26', 'call of duty', 'cyberpunk 2077', 'minecraft']
prices = [180, 140, 160, 120, 60]
for i,game in enumerate(games,1):
    print(f"{i}.{game}")

new_prices = [int(price*0.60) for price in prices]
print('\nTheas are the games that you are saving more than 50 lv')
for i in range(len(games)):                    
    saved = prices[i] - new_prices[i]       
    if saved > 50:
        print(f"{games[i].title()} you are saving {saved}lv.")





