from datetime import datetime as dt, timezone as tz, timedelta

"""
print(datetime.now())

# +00:00 - current time in UTC
today = datetime.now(timezone.utc)
print(today)

tomorrow = today + timedelta(days=1)
print(tomorrow)

print(type(today))
print(today.strftime("%d-%m-%Y %H:%M:%S"))

user_date = input("Enter the date in YYYY-mm-dd format: ")
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)
"""


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.registered = dt.now(timezone.utc)


# users = []

# user = {
#     'name': input('enter your name: '),
#     'location': input('enter your location: '),
#     'registered': dt.now(timezone.utc)
# }

# users.append(user)
# print(users)

now = dt.now(tz.utc)
# convert datetime obj to timestamp
current_timestamp = now.timestamp()
print(current_timestamp)

# back again
print(dt.utcfromtimestamp(current_timestamp))
