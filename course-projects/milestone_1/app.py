MENU_PROMPT = '''enter:
a: to add a new movie
l: to see your movies
f: find a movie by title
q: to quit
your choice: '''

movies = []


def add_movie():
    title = input('enter the movie title: ')
    director = input('enter the movie director: ')
    year = input('enter the movie release year: ')

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie in movies:
        show_movie(movie)


def show_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie(expected, finder):
    found = []

    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    return found


def find_movies():
    find_by = input('What property of the movie is that? ')
    looking_for = input('What are you looking for? ')

    result = find_movie(looking_for, lambda x: x[find_by])
    print(*result or "Not movies found!")


operations = {
    'a': add_movie,
    'l': list_movies,
    'f': find_movies
}


def menu():
    while True:
        user_choice = input(MENU_PROMPT)

        if user_choice in operations:
            operations[user_choice]()
        elif user_choice == 'q':
            print('Bye!')
            break
        else:
            print("Unknown command. Please try again!")


if __name__ == '__main__':
    menu()
