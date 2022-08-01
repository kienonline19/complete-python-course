"""
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_comsumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_comsumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_comsumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_comsumed": 235}
]


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_comsumed']
    return mpg


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    print_car_info(car)
"""

"""
def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(1, 2))
print(divide(1, 0))
"""


def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"

    return x / y


print(divide(1, 0))
print(divide(1, 2))
