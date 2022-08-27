import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file, delimiter='-')
    print(type(reader))

    for row in reader:
        print(row)
