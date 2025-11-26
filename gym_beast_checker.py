name = input("What is your name? ")
your_age = int(input("What is your age? "))
bench_press = int(input("What is your max bench press in 'kg'? "))
push_ups = int(input("How many push-ups you can do at once? "))
favorite_influensers = input("Who is your favorite influencer? ")

# Поправени списъци (без .strip() вътре!)
fitnes_influensers = ['Chris', 'Bumstead', 'Ronnie Coleman', 'Arnold', 'Jay Cutler', 'Sam Sulek']
banned_influensers = ['tosho', 'pencho_lifts', 'gosho_fit']
aproved_beasts = ['Hempata', 'Andrey', 'Denkata', 'Paco','Sezer']


if name.lower() in banned_influensers:
    print(f"{name} Get out of the gym!")
else:
    print(f"Wlcome to our gym {name.title()}!")

if name in aproved_beasts:
    print("WELCOME LEGEND!")

if bench_press >= 140:
    print("You are BEAST!")
elif bench_press >= 100:
    print("Nice keep the good work up.")
else:
    print("Traing harder!")

if push_ups >= 50:
    print("You are machine!")
elif push_ups >=30:
    print("Thats avarege but is okey.")
else:
    print("Search David Gogins in interner.")

hero = favorite_influensers.lower()
if 'Sam Sulek' in hero:
    print("You are just a chill guy.")
elif 'ronnie' in hero:
    print("YEAH BUDDY! LIGHT WEIGHT BABY!")
elif 'arnold' in hero:
    print("I'LL BE BACK...")
elif 'chris' in hero or 'bumstead' in hero or 'cbum' in hero:
    print("CBUM is King!")
else:
    print("Well you should tell us who it is.")


if name in aproved_beasts:
    print(f"{name} you are from ATLET GYM!")
elif bench_press >= 140 and push_ups >= 50 and name not in banned_influensers:
    print(f"Welcome to our gym {name.title()}!")
elif bench_press >= 100 or push_ups >= 40:
    print(f"{name} you are almost there")
else:
    print(f"{name} SOME DAY....")