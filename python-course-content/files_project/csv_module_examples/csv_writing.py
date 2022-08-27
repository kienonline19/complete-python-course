import csv

with open('temp.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='-')
    writer.writerow(['Name', 'Age', 'Profession'])
    writer.writerow(['Henry', 23, 'Artist'])
    writer.writerow(['Jack', 45, 'Engineer'])
    writer.writerow(['Jen', 30, 'Developer'])
    writer.writerow(['Bob', 12, 'Doctor'])
