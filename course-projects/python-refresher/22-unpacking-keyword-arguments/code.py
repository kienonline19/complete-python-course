"""
def named(**kwargs):
    print(kwargs)


named(name='Bob', age=34)
"""

# def named(name, age):
#     print(name, age)


# details = {'name': 'Bob', 'age': 25}
# named(**details)

# def named(**kwargs):
#     print(kwargs)


# details = {'name': 'Bob', 'age': 25}
# named(**details)

"""
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name='Bob', age=25)
"""

# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)


# nums = [1, 3, 5]
# details = {'name': 'Bob', 'age': 25}

# both(*nums, **details)

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""

# def add(y=3, x):
#     ...

def my_func(**kwargs): # kwargs must be mapping
    print(kwargs)


# my_func(**'Bob') # must be a mapping
my_func(**None)
