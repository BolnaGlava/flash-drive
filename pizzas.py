characters = {
    'gandalf': 'wizard',
    'vezuvi': 'wizard',
    'lord zul': 'wizard',
    'rabbit': 'animal',
    'sezer': 'human',
}
wizards = []

for name, kind in characters.items():
    if kind == 'wizard':
        wizards.append(name.title())


print("Finde the magician:")
for wizard in wizards:
    print(f"- {wizard}")
    
#TRY IT YOURSELF
#PIZAAAA
pizzas = ['caprichoza', 'camen', 'margarita']

for pizza in pizzas:
    print(f"{pizza.title()} is the best pizza in our restaurant!")
    print(f"I think pepperoni is better than {pizza.title()}!\n")

#ANIMALS
animals  = ['monkey','hamster','shark']
for i,animal in enumerate(animals,1):
    print(f'{i}.{animal} is going to be a great pet')
print("Any of this animals would make a great pet!")