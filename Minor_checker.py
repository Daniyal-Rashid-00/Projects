# Minnor Checker

while True:
    age = float(input("Enter age: "))

    if age >= 18:
        print("You are now considered an adult.")
    else:
        print("You are still a minor.")

    # repeat is only a Variable not a function
    repeat = input("Do you want to check another age? (y/n): ")

    if repeat.lower() != 'y':
        break

input("Program ended. Press Enter to exit...")