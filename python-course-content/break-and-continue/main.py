cars = ['ok', 'ok', 'ok', 'ok', 'faulty', 'ok']

for status in cars:
    if status == "faulty":
        # print("Stopping the production line!")
        # break

        print("Found faulty car, skipping ...")
        continue

    print(f"This car is {status}.")
    print("Shipping new car to customer!")
