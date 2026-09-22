user_list = ["tristan","lucas"]
password_list = ["123","qwe",]

def log_in():
    login_attempt = 0
    account_status = False
    while True:
        print()
        user_name = input("Enter your username: ")
        pass_word = input("Enter your password: ")

        if user_name in user_list and pass_word in password_list:
            for x,y in zip(user_list,password_list):
                if x == user_name and y == pass_word:
                    print(f"Welcome {user_name}")
                    account_status = True
                    break

        else: print("Wrong username or password")
        print()

        login_attempt += 1

        if login_attempt == 2 : print("You only have 1 remaining attempt to login again")
        elif login_attempt == 3:
            forgot_password = input("Forgot your password? ").lower()
            if forgot_password == 'y':
                #Username instead of verified email since we're just testing our coding skills, also we don't have that features yet
                user_name = input("Enter your username: ")
                for x,y in zip(user_list,password_list):
                    if x == user_name:
                        print(f"Your password is {y}, please try to login again")
                else:
                    if x != user_name:
                        print("We currently don't have it in our database. Please try again later, as you exceed 3 maximum attempt")
            else:
                print("Please try again later, as you exceed 3 maximum attempt")
                break
        if account_status == True:
            break
def sign_up():
    user_name = input("Enter username: ")
    pass_word = input("Enter password: ")
    user_list.append(user_name)
    password_list.append(pass_word)
    log_in()

account_status = input("Do you already have an account? ").lower()

for x in account_status:
    if x == 'y':
        log_in()
    elif x == 'n':
        sign_up()
    else: print("Invalid response")
    break

