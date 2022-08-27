file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]
for line in lines:
    name, age, university, degree = line.split(',') 

    print(f'{name.title()} is {age}, studying \
{degree.capitalize()} at {university.title()}.')

sample_csv_value = ','.join(['kenny', '30', 'mit', 'computer science'])

with open('csv_data.txt', 'a') as file_writing:
    file_writing.write(f'\n{sample_csv_value}\n')
