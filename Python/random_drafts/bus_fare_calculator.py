def calculate_fare(kilometers):
    if kilometers <= 4:
        pay = base_fare * discount
        if discount == 0.20:
            pay = base_fare + pay
        return pay

    elif kilometers > 4:
        added_km = kilometers - base_km
        total_fare = base_fare + (added_km * additional_fare)
        net_price = total_fare * discount
        if discount == 0.20:
            net_price = total_fare - net_price

        return net_price

    else:
        return "Invalid Input"

base_fare = 13
base_km = 4
additional_fare = 1.80
answer = ["y", "n"]

while True:
    try:
        user_type = input("Are you a regular passenger? (Yes/No, or 'q' to quit): ").lower()
        if user_type == "q":
            break
        km = int(input("How many kilometers: "))

        if km < 1:
            raise ValueError("Please enter at least 1 km.")
        if user_type[0] not in answer:
            raise ValueError("Please Answer yes or No only")

    except ValueError as e:
        if str(e) == "Please enter at least 1 km.":
            print(e)
        elif str(e) == "Please Answer yes or No only":
            print(e)
        else:
            print("Only Number is allowed")

    else:
        if user_type[0] == "y":
            discount = 1
        else:
            discount = .20

        total_cost = calculate_fare(km)
        print(f"Your total fare is: ₱{total_cost}")
    print()

print("Thanks for using our app! Have a safe trip.")