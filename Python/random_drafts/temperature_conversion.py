user_choice_input = input("Convert to Celsius or Fahrenheit (C/F): ").lower()
temp = float(input("Enter a number: "))


if user_choice_input[0] == "c":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"Temperature in Fahrenheit: {temp}°F")

elif user_choice_input[0] == "f":
    temp = round((temp - 32 ) * 5/9, 1)
    print(f"Temperature in Celsius: {temp}°C")

else:
    print(f"{user_choice_input} is invalid conversion")