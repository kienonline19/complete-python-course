import re
import datetime

MAIN_MENU_PROMPT = """Please enter 1 for Sign up.
Please enter 2 for Log in.
Please enter 3 for Exit.
"""

SUB_MENU_PROMPT = """Please enter 1 for Resetting the Password.
Please enter 2 for Signout.
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
    user_option = int(input(MAIN_MENU_PROMPT))

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
                if email_id not in past:
                    users.append(SignUp(
                        full_name,
                        email_id,
                        mobile_number,
                        password,
                        date_of_birth
                    ).__dict__)

                past.add(email_id)
                print("You have Successfully Signed up.")
                break

    elif user_option == 2:
        user_name = input("Please enter your Username (Mobile Number):")
        print()
        user_password = input("Please enter your password:")

        if len(users) != 0:
            for user in users:
                if user['mobile_number'] == user_name and \
                        user['password'] == user_password:
                    print("You have successfully Signed in")
                    print(f"Welcome {user['full_name']}")

                    sub_user_option = int(input(SUB_MENU_PROMPT))
                    if sub_user_option == 1:
                        flag = False

                        for _ in range(3):
                            sub_user_name = input(
                                "Please enter your Username (Mobile Number):")
                            print()
                            old_password = input(
                                "Please enter your old password:")
                            print()
                            new_password = input(
                                "Please enter your new password:")
                            check = bool(re.match(r'[A-Za-z]+[@$#]+\d+', new_password))

                            if sub_user_name == user_name and \
                                    check and \
                                    old_password == user_password:
                                user['password'] = new_password
                                print("Your Password has been reset successfully.")
                                flag = True
                                break

                        if not flag:
                            print("You have used the maximum attempts of Login:")
                            print("Please reset the password by entering the below details\n")

                            username_mn = input("Please enter your Username (Mobile Number) to confirm:")
                            flag1 = user_name != username_mn
                            if flag1:
                                print("You have entered the wrong Username.")

                            print()
                            dob = input("Please enter your Date of Birth in DD/MM/YYYY format, to confirm:")
                            flag2 = dob != user['date_of_birth']
                            if flag2:
                                print("You have entered the wrong Date of Birth.")

                            print()
                            n_pass = input("Please enter your new password:")
                            flag3 = not re.match(r'[A-Za-z]+[@$#]+\d+', n_pass)
                            if flag3:
                                print("You have entered the new password in Invalid format.")

                            print()
                            re_pass = input("Please re-enter your new password:")
                            flag4 = re_pass != n_pass
                            if flag4:
                                print("Your passwords are not matching.")

                            if n_pass == user_password:
                                print("You cannot use the password used earlier.")
                                break
                            elif all(flag == False for flag in (flag1, flag2, flag3, flag4)):
                                print("Your Password has been reset successfully.")
                                user['password'] = n_pass
                            else:
                                break

                    elif sub_user_option == 2:
                        print("Thank You for using the Application.")
                        break

    elif user_option == 3:
        print("Thank You for using the Application.")
        break
