"""
def greet():
    print("Hello")


# hello = greet
# hello()

def before_and_after(func):
    print("Before...")
    func()
    print("After")


# before_and_after(5) - TypeError: int object is not callable
before_and_after(lambda: 5)
before_and_after(greet)
"""

movies = [ 
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"}
]


def find_movie(expected_value, finder):
    found = []

    for movie in movies:
        if expected_value == finder(movie):
            found.append(movie)

    return found


find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movies = find_movie(looking_for, lambda movie: movie[find_by])

print(movies or "No movies found.")


