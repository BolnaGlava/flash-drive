cars = ["Lamborghini Aventador", "Ferrari 488", "Porsche 911", 
        "Tesla Model S Plaid", "BMW M8", "Audi RS7"]
print("ALL IN CAPS LOCK")
for car in cars:
    print(car.upper())
    print(f"{car.upper()} all in caps lock!")
    
cars[3] = "Bugatti Chiron"
print(cars)
cars.append("Golf 7")
print(f"This is the one {cars[-1]} I want the MOST!!!")
print(len(cars))
print("\nDone! My dream garage is ready!")