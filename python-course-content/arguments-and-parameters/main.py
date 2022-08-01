car = 'Hello'

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_comsumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_comsumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_comsumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_comsumed": 235}
]


def calculate_mpg(car, intro):
    print(intro)
    mpg = car['mileage'] / car['fuel_comsumed']
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    calculate_mpg(car, "New Car")
