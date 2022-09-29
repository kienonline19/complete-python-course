"""
* counter
* namedtuple
* defaultdict
* ordereddict
* deque
"""
# counter
"""
from collections import Counter

device_temperatures = [13.5, 14.0, 14.5, 14.5, 14.5, 15.0, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)

print(temperature_counter[14.0])
print(temperature_counter[14.5])
print(temperature_counter.most_common(1)[0][0])

print(Counter({"hello": 5, "hi": 3})["hi"])
"""

# defaultdict
# my_dict = {"hello": 5}
# print(my_dict["hi"]) # KeyError: 'hi'

from collections import defaultdict

"""
coworkers = [ 
    ('Rolf', 'MIT'),
    ('Jen', 'Oxford'),
    ('Rolf', 'Cambridge'),
    ('Charlie', 'Manchester')
]

alma_maters = defaultdict(list) # list(), User()

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# print(alma_maters['Rolf'])
# print(alma_maters['Anna'])

alma_maters.default_factory = None
alma_maters.default_factory = int
print(alma_maters['Rolf'])

# raise error when access to key not exists
print(alma_maters['Anna'])

# alma_maters = {}

# for coworker, place in coworkers:
#     if coworker not in alma_maters:
#         alma_maters[coworker] = []

#     alma_maters[coworker].append(place)

# print(alma_maters)
"""

"""
my_company = 'Teclado'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']

other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])
"""

"""
from collections import OrderedDict

d = OrderedDict()
d['Rolf'] = 6
d['Jose'] = 12
d['Jen'] = 3

print(d)
d.move_to_end('Rolf')
print(d)

d.move_to_end('Rolf', last=False)
print(dict(d))

tup = d.popitem()
print(tup)
print(d)

tup = d.popitem(last=False)
print(tup)
"""

"""
from collections import namedtuple

account = ('checking', 1850.90)

# print(account[0]) # name
# print(account[1]) # balance

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)

print(account.name)
print(account.balance)

print(account)

print(account[0])
print(account[1])

name, balance = account
print(name)
print(balance)

account = Account('checking', balance=1850.9)
print(account)

acc_named_tuple = Account._make(account)
print(acc_named_tuple)

acc = Account(*account)
print(acc)

print(acc._asdict()['balance'])
"""

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Anna', 'Bob'))
friends.append("Jen")
friends.appendleft("Anthony")

print(friends)

lperson = friends.pop()
print(lperson)

print(friends)
sperson = friends.popleft()
print(sperson)

print(friends)

