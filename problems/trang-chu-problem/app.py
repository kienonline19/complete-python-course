import re
import datetime

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

DINE_IN_MODE = """Enter 1  for Noodles\tPrice AUD 2
Enter 2  for Sandwich\tPrice AUD 4
Enter 3  for Dumpling\tPrice AUD 6
Enter 4  for Muffins\tPrice AUD 8
Enter 5  for Pasta\tPrice AUD 10
Enter 6  for Pizza\tPrice AUD 20
Enter 7  for Coffee\tPrice AUD 2
Enter 8  for Colddrink\tPrice AUD 4
Enter 9  for Shake\tPrice AUD 6
"""


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
                    home_page_option = input(HOME_PAGE)

                    if home_page_option == '2.1':

                        order_option = input(ORDERING_PAGE)

                        if order_option == '1': # dine in mode

                            dine_in_option = input(DINE_IN_MODE)

                        elif order_option == '2': # order online

                            order_online_option = input(ORDER_ONLINE_PAGE)

                            if order_online_option in set('12'): # click and collect and delivery
                                food_option = input(FOOD_MENU)
                            elif order_online_option == '3': # go to previous menu
                                pass

                        elif order_option == '3': # go to login page
                            pass

                    elif home_page_option == '2.2':
                        pass
                    elif home_page_option == '2.3':
                        pass

    elif user_option == 3:
        print("Thank You for using the Application.")
        break
