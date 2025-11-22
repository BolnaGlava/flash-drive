name = input("Whats your name? ")
age = int(input("How old are you? "))
money_now = float(input("How much money do you have right now? "))
monthly_save = float(input("How much do you save every month? "))
#Calculating how much money the user will have after 12 months?
after_year = money_now + (monthly_save * 12)
PlayStation5 = 1200
iPhone_16 = 3000
show_ticket = 100

amount_ps5 = after_year / PlayStation5
amount_iphone = after_year / iPhone_16
amount_ticket = after_year / show_ticket

#Exit 
print("\n" + "=" * 50)
print(f"Hello, {name}!")
print(f"After 12 months of saving you will have {after_year}")
print(f"Whit this money you can buy this things:")
print(f"{amount_ps5} number of ps5")
print(f"{amount_iphone} numbers of iphones")
print(f"{amount_ticket} number of tickets")