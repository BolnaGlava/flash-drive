#PROGRAM INTERWIE FOR COMPANY
age = int(input("How old are you? "))
savings = int(input("How much money do you have saved?" ))
favorite_car = input("Whats ypu favorite car?" )
cars = ['golf','lambo','porsche','tesla']
if age < 18:
    print("You're still too young, bro, learn Python first.")
elif age > 30:
    print("You're too old for an internship, but maybe you'd fit a junior position.")
else:
    print("You are in!")
if savings < 5000:
    print('Nothing happens without money, keep saving up.')
if favorite_car.lower() == 'golf':
    print("+100 points (you are totally on the wave)")
elif favorite_car.lower() == 'lambo':
    print('Ambition is cool, but first get that paycheck.')
elif favorite_car.lower() == 'tesla':
    print("Eco-thinking, we like you")
else:
    print("The main thing is to love cars, we'll figure the rest out")
if age >= 18 and age <= 30 and savings >= 500 and favorite_car in ['golf', 'lambo', 'tesla', 'porsche']:
    print("\nWE'RE TAKING YOU ON AS AN INTERN AT LIMECAIN!")
else:
    print("\nNot yet, but keep going — it’ll happen!")