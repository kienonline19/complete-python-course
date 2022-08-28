"""
[{"club": "Manchester United", "country": "UK", "city": "Manchester"}, 
{"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, 
{"club": "Juventus", "country": "Italy", "city": "Turin"}]
"""
import json

csv_file = open('csv_file.txt', 'r')
csv_data = [line.strip() for line in csv_file.readlines()]
csv_file.close()

result = []

for line in csv_data:
    club, city, country = line.split(',')
    result.append({
        'club': club,
        'country': country,
        'city': city
    })

json_file = open('json_file.txt', 'w')
json.dump(result, json_file)
json_file.close()
