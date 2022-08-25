# Ask the user for a list of three friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'
# hint: readlines()
friends = input('Enter three friend names, separated by commas (no spaces, please): ').\
    split(',')

people = open('people.txt', 'r')
print(type(people))
people_nearby_set = {person.strip() for person in people.readlines()}
people.close()

friends_nearby = '\n'.join(people_nearby_set.intersection(friends))

nearby_friends_file = open('nearby_friends.txt', 'w')
nearby_friends_file.write(friends_nearby)
nearby_friends_file.close()
