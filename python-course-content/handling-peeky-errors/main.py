def power_of_two():
    user_input = input('Please enter a number: ')
    
    try:
        n = float(user_input)
        
        n_square = n ** 2,
        return n_square
    except ValueError:
        print('Invalid input!')
        return 0
    except RuntimeError:
        ...

    
print(power_of_two())
print(power_of_two())
