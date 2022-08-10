import re
import datetime
import random
import string

MAIN_MENU_PROMPT = """Please enter 1 for Sign up.
Please enter 2 for Log in.
Please enter 3 for Exit.
"""

HOME_PAGE = """  Please Enter 2.1 to Start Ordering.
  Please Enter 2.2 to Print Statistics.
  Please Enter 2.3 for Logout.
"""

ORDERING_PAGE = """  Please Enter 1 for Dine in.
  PLease Enter 2 or Order Online.
  Please Enter 3 to go to Login Page.
"""

ORDER_ONLINE_PAGE = """Enter 1 for Self Pickup.
Enter 2 for Home Delivery.
Enter 3 to go to Previous Menu.
"""

FOOD_MENU = """Enter 1  for Noodles\tPrice AUD 2
Enter 2  for Sandwich\tPrice AUD 4
Enter 3  for Dumpling\tPrice AUD 6
Enter 4  for Muffins\tPrice AUD 8
Enter 5  for Pasta\tPrice AUD 10
Enter 6  for Pizza\tPrice AUD 20
Enter 7 for Drinks Menu:
"""

DRINK_MENU = """Enter {}  for Coffee\tPrice AUD 2
Enter {}  for Colddrink\tPrice AUD 4
Enter {}  for Shake\tPrice AUD 6
"""

DINE_IN_MODE = f"""Enter 1  for Noodles\tPrice AUD 2
Enter 2  for Sandwich\tPrice AUD 4
Enter 3  for Dumpling\tPrice AUD 6
Enter 4  for Muffins\tPrice AUD 8
Enter 5  for Pasta\tPrice AUD 10
Enter 6  for Pizza\tPrice AUD 20
{DRINK_MENU.format(7, 8, 9)}"""

TRANSACTIONS = """ Please Enter the Option to Print the Statistics.
 1 - All Dine in Orders.
 2 - All Pick up Orders.
 3 - All Deliveries.
 4 - All Orders (Descendingly based on Order ID).
 5 - Total Amount Spent on All Orders.
 6 - To go to Previous Menu.
"""

ORDERING = {
    1: ('noodeles', 2),
    2: ('sandwich', 4),
    3: ('dumpling', 6),
    4: ('muffins', 8),
    5: ('pasta', 10),
    6: ('pizza', 20),
    7: ('coffee', 2),
    8: ('colddrink', 4),
    9: ('shake', 6)
}


class SignUp:
    def __init__(self, name, address, mobile_number, password, password_confirm, date_of_birth):
        self.name = name
        self.mobile_number = mobile_number
        self.password = password
        self.password_confirm = password_confirm
        self.date_of_birth = date_of_birth
        self.address = address

    @classmethod
    def process_signup(cls, info):
        name, address, mobile_number, password, password_confirm, date_of_birth = info
        signup = None

        while True:
            flag_mobile_number = len(mobile_number) != 10 or \
                not mobile_number.isdigit() or \
                not mobile_number.startswith('0')

            flag_password = not re.match(r'[A-Za-z]+[@$#]+\d+', password)
            flag_password_confirm = not (password == password_confirm)
            flag_age = True

            try:
                datetime.datetime.strptime(date_of_birth, r'%d/%m/%Y')
                flag_date_of_birth = False

                current_year = datetime.datetime.now().year
                birthyear = int(date_of_birth.split(r'/')[-1])
                age = current_year - birthyear

                if age >= 18:
                    flag_age = False

            except ValueError:
                flag_date_of_birth = True

            if flag_mobile_number:
                print("You have entered the mobile number in invalid format.")
                mobile_number = input("Please start again::")
                print()

            if flag_password:
                print("You have entered the Password in invalid format.")
                password = input("Please start again:")
                print()

            if flag_password_confirm:
                print("Your passwords are not matching.")
                password_confirm = input("Please start again:")
                print()

            if flag_date_of_birth or flag_age:
                print("You have entered the Date of Birth in invalid format.")
                date_of_birth = input("Please start again:")
                print()

            if all(
                    flag == False
                    for flag in (flag_mobile_number, flag_password, flag_password_confirm, flag_date_of_birth, flag_age)
            ):
                info = (name, address, mobile_number, password,
                        password_confirm, date_of_birth)
                print('You have Successfully Signed up.')
                signup = cls(*info)
                break

        return signup


class Order:
    def __init__(self, order_id, order_date, type_of_order, order_amount=0):
        self.id = order_id
        self.date = order_date
        self.order_type = type_of_order
        self.amount = order_amount

    def __str__(self) -> str:
        return f"{self.id}\t\t{self.date}\t\t{self.order_type}\t\t{self.amount}"


def print_list_orders(orders):
    print('Order ID\t\tDate\t\tType of Order\t\tOrder Amount')
    for order in orders:
        print(order)


def random_order_id(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_dine_in_order_input():
    date_dinein = input('Please enter the Date of Booking for Dine in:')
    time_dinein = input('Please enter the Time of Booking for Dine in:')
    num_persons = input('Please enter the Number of Persons:')

    return (date_dinein, time_dinein, num_persons)


def get_pickup_order_input():
    date_pickup = input('Please enter the Date of Pick up:')
    time_pickup = input('Please enter the Time of Pick up:')
    name = input('Please enter the Name of the Persons:')

    return (date_pickup, time_pickup, name)


def get_delivery_order_input():
    date_delivery = input('Please enter the Date of Delivery:')
    time_delivery = input('Please enter the Time of Delivery:')
    distance = float(input('Please enter the Distance from the restaurant:'))

    return (date_delivery, time_delivery, distance)


def get_user_input():
    name = input('Please enter your name:')
    print()

    address = input('Please enter your address or press enter to Skip.')
    print()

    # 0111111234
    mobile_number = input("Please enter your mobile number:")
    print()

    # Sam@#$1234
    password = input("Please enter your Password:")
    print()

    # same above
    password_confirm = input("Please confirm your Password:")
    print()

    # 11/11/1999
    date_of_birth = input(
        "Please Enter your Date of Birth # DD/MM/YYYY (No Space):")

    return (name, address, mobile_number, password, password_confirm, date_of_birth)


users = []

while True:
    user_option = int(input(MAIN_MENU_PROMPT))

    if user_option == 1:
        info = get_user_input()
        user = SignUp.process_signup(info)
        users.append(user.__dict__)

    elif user_option == 2:
        user_name = input("Please enter your Username (Mobile Number):")
        print()
        user_password = input("Please enter your password:")

        if len(users) != 0:
            new_user = None

            for user in users:
                if user['mobile_number'] == user_name and \
                        user['password'] == user_password:
                    new_user = user
                    print("You have successfully Signed in")
                    break

            if new_user is not None:
                orders = []

                while True:
                    home_page_option = input(HOME_PAGE)

                    if home_page_option == '2.1':  # start ordering

                        order_option = int(input(ORDERING_PAGE))

                        if order_option == 1:  # dine in mode

                            items = []

                            while True:
                                food_drink_option = int(
                                    input(DINE_IN_MODE))

                                items.append(
                                    ORDERING.get(food_drink_option))

                                if food_drink_option == 4:
                                    yn_checkout = input('PLease Enter Y to proceed to Checkout or\
                                                \n Enter N to cancel the order:').\
                                        upper()

                                    if yn_checkout == 'Y':
                                        total_amount = sum(
                                            item[1] for item in items)

                                        extra = 0.1 * total_amount
                                        total_amount += extra

                                        print(
                                            f"Your total payable amount: {total_amount} including AUD {extra} for Service Charges")

                                        # create order
                                        order_id = random_order_id()

                                        dinein_date, dinein_time, nums = get_dine_in_order_input()
                                        dinein_order = Order(order_id,
                                                             f"{dinein_date} {dinein_time}",
                                                             "dine-in",
                                                             total_amount)

                                        orders.append(dinein_order)
                                        print(
                                            f'Thank You for entering the details, Your Booking is confirmed\n\
and your order id is {order_id}')

                                    break

                        elif order_option == 2:  # order online

                            order_online_option = int(input(
                                ORDER_ONLINE_PAGE))

                            # click and collect and delivery
                            # home delivery and self pickup
                            if order_online_option in {1, 2}:
                                items = []

                                while True:
                                    food_option = int(input(FOOD_MENU))

                                    items.append(
                                        ORDERING.get(food_option))

                                    if food_option == 7:  # select drinks

                                        while True:

                                            drink_option = int(input(DRINK_MENU.format(1, 2, 3) +
                                                                     'Enter 4 for Checkout:\n'))

                                            items.append(
                                                ORDERING.get(10 - drink_option))

                                            if drink_option == 4:
                                                break

                                        if order_online_option == 2 and user['address'] == '':

                                            yn_address = input('You have not mentioned your address, while signing up.\
                                            \nPlease Enter Y if would like to enter your address.\
                                            \nEnter N if you would like to select other mode of order:').upper()

                                            if yn_address == 'Y':
                                                while new_user['address'] == '':
                                                    address = input(
                                                        'Please enter your address:')
                                                    new_user['address'] = address

                                                    for user in users:
                                                        if user['mobile_number'] == new_user['mobile_number'] and \
                                                                user['password'] == new_user['password']:
                                                            user['address'] = new_user['address']
                                                            break

                                            elif yn_address == 'N':
                                                break

                                        if drink_option == 4:  # checkout

                                            yn_checkout = input('PLease Enter Y to proceed to Checkout or\
                                            \n Enter N to cancel the order:').\
                                                upper()

                                            if yn_checkout == 'Y':

                                                total_amount = sum(
                                                    item[1] for item in items)

                                                if order_online_option == 2:
                                                    distance = float(
                                                        input())
                                                    while distance <= 0:
                                                        distance = float(
                                                            input())

                                                    if distance <= 2:
                                                        total_amount += 5
                                                    elif distance <= 5:
                                                        total_amount += 10
                                                    elif distance <= 10:
                                                        total_amount += 18
                                                    else:
                                                        break

                                                print(f"Your total payable amount: {total_amount}\
{' and there will be an additional charges for Delivery.' if order_online_option == 2 else ''}")

                                                order = None
                                                order_id = random_order_id()

                                                if order_online_option == 1:  # self pickup

                                                    # create order
                                                    date_pickup, time_pickup, name = get_pickup_order_input()
                                                    order = Order(order_id,
                                                                  f"{date_pickup} {time_pickup}",
                                                                  "pick-up",
                                                                  total_amount)

                                                    print(
                                                        f'Thank You for entering the details, Your Booking is confirmed\n\
and your order id is {order_id}')

                                                elif order_online_option == 2:  # online order

                                                    # create order
                                                    date_delevery, time_delivery, kms = get_delivery_order_input()

                                                    if kms > 10:
                                                        print(
                                                            'Please, pick up to Order')
                                                        break

                                                    order = Order(order_id,
                                                                  f"{date_delevery} {time_delivery}",
                                                                  "delivery",
                                                                  total_amount)
                                                    print(
                                                        f'Thank You for your order, Your Order has been confirmed\n\
and your order id is {order_id}')

                                                if order is not None:
                                                    orders.append(
                                                        order)
                                            break

                            elif order_online_option == 3:  # go to previous menu
                                break

                        elif order_option == 3:  # go to login page
                            break

                    elif home_page_option == '2.2':  # print statistics

                        if orders:
                            user_choice = int(input(TRANSACTIONS))

                            conditions = ('dine-in', 'pick-up', 'delivery')

                            if user_choice in {1, 2, 3}:
                                new_orders = [
                                    order for order in orders if order.order_type == conditions[user_choice - 1]]
                                print_list_orders(new_orders)
                            elif user_choice == 4:  # all orders (desc)
                                new_orders = sorted(
                                    orders, key=lambda x: x.id, reverse=True)
                                print_list_orders(new_orders)
                            elif user_choice == 5:  # total amount
                                total_amount = sum(x.amount for x in orders)
                                print(
                                    f'Total amount spent on all orders AUD: {total_amount}')
                            elif user_choice == 6:  # go to previous menu
                                break

                    elif home_page_option == '2.3':  # logout
                        break

    elif user_option == 3:
        print("Thank You for using the Application.")
        break
