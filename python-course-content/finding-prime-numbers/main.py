for n in range(2, 10):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")
