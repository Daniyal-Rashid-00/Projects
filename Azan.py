#welcome to the biggest and the most famouse crpto currency store in the world you can get many coins with the best price and offers


print("Welcome to the Meow Crypto Store!")

name = input("BTW what's your name?\n")

if name == "Daniyal" or name == "daniyal":
    cringe_status = input("Are you cringe?\n")

    aura_status = int(input("How much Aura do you have?\n"))

    if cringe_status == "yes" and aura_status < 1000:

        print("Your not welcome here!. " + name + " SHO SHO!!")

        input()

    else:

        print("Hello " + name +", thank you for coming to Meow Crypto store!.\n\n")

else:

    print("Hello " + name +", thank you for coming to Meow Crypto store!.\n\n")

    coin_collection = "1.bitcoin 2.ethereum 3.litcoin 4.dogecoin 5.tether"

    print(name + ", what would you like to buy today? Here are the available coins.\n" + coin_collection)

coin_choice = input()

if coin_choice == "bitcoin" or "1":
    price = 10

elif coin_choice == "ethereum":
    price = 8

elif coin_choice == "litcoin":
    price = 5

elif coin_choice == "dogecoin":
    price = 7

elif coin_choice == "tether":
    price = 9
else:
    print("Sorry, wo don't have that.")

    input()

    exit

print(price)

quantity = input("How many " + coin_choice + " would you like to buy? \n")

total = price * int(quantity)

print("Thank you." + name + " Your total is: $" + str (total))

print("Sound Good " + name + "! we'll have your" + " " + coin_choice + " BTW " + coin_choice + " is very popular right now" + " and ready for you in a moment.\n")

input() 
