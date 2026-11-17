# check if it has uppercase, lowercase, digit, hash, and long enough
def check_password(password):
    is_long = [len(password) >= 8, "More than 7 characters"]
    has_lowercase = [any(letter.islower() for letter in password), "At least One Lowercase"]
    has_uppercase = [any(letter.isupper() for letter in password), "At least One Uppercase"]
    has_digit = [any(number.isdigit() for number in password), "At least One Number"]
    has_hash = [any(each == "#" for each in password), "At least One hash (#)"]

    password_layers = [is_long, has_lowercase, has_uppercase, has_digit, has_hash]

    if is_long[0] and has_lowercase[0] and has_uppercase[0] and has_digit[0] and has_hash[0]:
        return "Strong Password"

    else:
        print()
        print("Your password should have the Following:")
        i = 1
        for layer in password_layers:
            if layer[0] == False:
                print(f"{i}. {layer[1]}")
                i += 1
        return "Please try again"

while True:
    password_input = input("Enter your password: ")
    result = check_password(password_input)
    print()
    print(result)

    if result == "Strong Password":
        break