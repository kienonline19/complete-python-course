import re
import datetime

MENU_PROMPT = """Please enter 1 for Sign up.
Please enter 2 for Log in.
Please enter 3 for Exit.
"""


class SignUp:
    def __init__(self, full_name, email_id, mobile_number, password, date_of_birth):
        self.full_name = full_name
        self.email_id = email_id
        self.mobile_number = mobile_number
        self.password = password
        self.date_of_birth = date_of_birth


users = []
past = set()

while True:
    user_option = int(input(MENU_PROMPT))

    if user_option == 1:
        full_name = input("Please enter your name:")
        print()

        email_id = input("Please enter email ID:")
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

        # 11/11/2021
        date_of_birth = input(
            "Please Enter your Date of Birth # DD/MM/YYYY (No Space):")

        while True:

            flag_mobile_number = len(mobile_number) != 10 or \
                not mobile_number.isdigit() or \
                not mobile_number.startswith('0')

            flag_password = not re.match(r'[A-Za-z]+[@$#]+\d+', password)
            flag_password_confirm = not(password == password_confirm)
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
                if email_id not in past:
                    users.append(SignUp(
                        full_name,
                        email_id,
                        mobile_number,
                        password,
                        date_of_birth
                    ))

                past.add(email_id)
                print("You have Successfully Signed up.")
                break

    elif user_option == 2:
        pass
    elif user_option == 3:
        print("Thank You for using the Application.")
        break
