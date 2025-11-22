#22.11.2025г.
#first list 
names = ['hempa','adnro','rija','vezul']
print (names[0])
print(f'{names[0].title()} you are my best friend!')
#pop method
cars = ["honda","bmw","audi"]
poped_cars = cars.pop(0)
print(poped_cars)

#TRY IT YOUR SELF
guest_list = ['ramon','miro','denko']
print(f'{guest_list[0].title()} you are welcome in my house!')
print(f"{guest_list[1].title()} won't be able to come to dinner with us tonight.")
busy=guest_list.pop(1)
print(busy.title())
guest_list.append('venelin')
print(guest_list)
print(f"{guest_list[0]} i am informing you that i found a bigger table!")
print(f"{guest_list[1]} i am informing you that i found a bigger table!")
print(f"{guest_list[2]} i am informing you that i found a bigger table!")
guest_list.insert(0,'zul')
busy=guest_list.pop(0)
busy=guest_list.pop(2)
print(f'{busy} sorry i cant invite you.')
print(guest_list)