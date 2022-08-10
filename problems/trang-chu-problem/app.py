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
        return ''


def random_order_id(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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
        print(users[0])

    elif user_option == 2:
        user_name = input("Please enter your Username (Mobile Number):")
        print()
        user_password = input("Please enter your password:")

        if len(users) != 0:
            for user in users:
                if user['mobile_number'] == user_name and \
                        user['password'] == user_password:
                    print("You have successfully Signed in")

                    while True:
                        home_page_option = input(HOME_PAGE)
                        orders = []

                        if home_page_option == '2.1':  # start ordering

                            while True:
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

                                            elif yn_checkout == 'N':
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
                                                        while user['address'] == '':
                                                            address = input(
                                                                'Please enter your address:')
                                                            user['address'] = address
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
                                                            while distance <= 0 or distance > 10:
                                                                distance = float(
                                                                    input())

                                                            if distance <= 2:
                                                                total_amount += 5
                                                            elif distance <= 5:
                                                                total_amount += 10
                                                            else:
                                                                total_amount += 18

                                                        print(f"Your total payable amount: {total_amount}\
{' and there will be an additional charges for Delivery.' if order_online_option == 2 else ''}")

                                                    elif yn_checkout == 'N':
                                                        break

                                    elif order_online_option == 3:  # go to previous menu
                                        break

                                elif order_option == 3:  # go to login page
                                    break

                        elif home_page_option == '2.2':  # print statistics
                            pass
                        elif home_page_option == '2.3':  # logout
                            break

    elif user_option == 3:
        print("Thank You for using the Application.")
        break
