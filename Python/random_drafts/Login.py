list_of_users = []

def log_in():
    login_attempt = 0
    login = True


    while login:
        print()
        print(f"Log-in attempt ({login_attempt}/3)")
        user_name = input("Enter your username: ")
        pass_word = input("Enter your password: ")

        for user in list_of_users:
            if user_name == user["username"] and pass_word == user["password"]:
                print(f"Welcome {user_name}")
                login = False
                break
        else:
            print("Wrong username or password")
            login_attempt += 1
            print()
        if not login:
            break

        if login_attempt == 4:
            # Username login used for testing; email verification not yet supported
            forgot_password = input("Forgot your password? ").lower()

            if forgot_password[0] == 'y':
                user_name = input("Enter your username: ")
                for user in list_of_users:
                    if user_name == user["username"]:
                        print(f"Your password is {user["password"]}, please try to login again")
                        break
                else:
                    print("Record not found. Maximum attempts (3/3) exceeded. Please try again later.")
                    break
            else:
                print("Maximum attempts (3/3) exceeded. Please try again later.")
                break

def sign_up():
    user_name = input("Enter username: ")
    pass_word = input("Enter password: ")
    create_account = {
        "username": user_name,
        "password": pass_word
    }

    list_of_users.append(create_account)
    log_in()

account_status = input("Do you already have an account? ").lower()


if account_status[0] == 'y':
    log_in()
elif account_status[0] == 'n':
    sign_up()
else:
    print("Invalid response")