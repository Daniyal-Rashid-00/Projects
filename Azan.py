#welcome to the biggest and the most famouse crpto currency store in the world you can get many coins with the best price and offers


print("Welcome to the Meow Crypto Store!")

name = input("BTW what's your name?\n")

allowed = True

if name.lower() == "daniyal":
    cringe_status = input("Are you cringe? (yes/no)\n").lower()

    if cringe_status == "yes":
        aura_status = int(input("How much Aura do you have?\n"))

        if aura_status < 1000:
            print("You're not welcome here, " + name + "! SHO SHO!!")
            allowed = False

# Continue only if allowed
if allowed:
    print("\nHello " + name + ", thank you for coming to Meow Crypto Store!")
    
    coin_collection = (
        "1. Bitcoin\n"
        "2. Ethereum\n"
        "3. Litecoin\n"
        "4. Dogecoin\n"
        "5. Tether"
    )

    print("\nWhat would you like to buy today? Here is our menu:\n")
    print(coin_collection)


    coin_choice = input("\nEnter coin name or number: ").lower()

    if coin_choice == "bitcoin" or coin_choice == "1":
        price = 10
        coin_choice = "Bitcoin"

    elif coin_choice == "ethereum" or coin_choice == "2":
        price = 8
        coin_choice = "Ethereum"

    elif coin_choice == "litecoin" or coin_choice == "3":
        price = 5
        coin_choice = "Litecoin"

    elif coin_choice == "dogecoin" or coin_choice == "4":
        price = 7
        coin_choice = "Dogecoin"

    elif coin_choice == "tether" or coin_choice == "5":
        price = 9
        coin_choice = "Tether"

    else:
        print("Sorry, we don't have that coin.")
        exit()

    quantity = int(input("How many " + coin_choice + " would you like to buy?\n"))
    total = price * quantity

    print("\nThank you, " + name + "!")
    print("Your total is: $" + str(total))
    print("Sounds good, " + name + "! Your " + coin_choice +
        " Sounds good, " + name + "! Your " + coin_choice + " is very popular right now and will be ready shortly!")

input() 
