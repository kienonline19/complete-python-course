import json

file = open('friends_json.txt', 'r')

# load json file to dictionary
# load(file pointer) - reads file and turns it to dict
file_contents = json.load(file)
file.close()

print(file_contents['friends'][0])

cars = [ 
    { 'make': 'Ford', 'model': 'Fiesta' },
    { 'make': 'Ford', 'model': 'Focus' },
]

# json.dump - write list dicts/dict to file
out_file = open('cars_json.txt', 'w')
json.dump(cars, out_file)
out_file.close()

#=================================================================
# loads - convert json string to dict
json_string = '[{"name": "Alfa romeo", "released": 1996}]'
incorrect_car = json.loads(json_string)

print(incorrect_car[0]['name'])

# dumps - convert dict to json string
print(json.dumps(incorrect_car, indent=4))
