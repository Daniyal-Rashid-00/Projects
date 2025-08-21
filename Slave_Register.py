# Slave Registor

while True:
    print("***Slave Registration Office***")
    name = input("\nType your name (Future) Slave: ")
    if name.lower() == "daniyal" or name.lower() == "mama":
        # The .lower makes any input of the word daniyal lower case.

        print("\nBoss why are you typing your name?\nDon't worry we will get all the Slaves ready in no time boss")
        input("Enter to Close...")
        exit
    else:
        print("\nThe new slave has been registered as: " + name)

    # Slave type:
    print("\nWhat type of slave do you want to be?")
    type = input()
    print("\nOK " + name + " ,You wrote " + type + " ,so you have been Registered as a " + type + " Permanent Slave.")

    # Slave Properties
    age = input("Enter Your Age...Slave!\n")
    Brain = input("OK, Do you have a brain...Slave???\n")
    strong = input("OK, Are you Strong?...Slave???\n")
    print("\nOK, " + name + ", you wrote your age is " + age + ", and specially you wrote you have " + Brain + " Brains and you have: " + strong + " Strength, Hmm... \nYou are probably a big DUM DUM and Weak Slave!!! But Don't worry, You will do.")

    # Slave Salary:
    salary = 50
    print("\nYour salary is 50 Per Day!")
    day = input("How many days will you work? (Probably forever) :...")
    total = salary * int(day)
    print("\nYour Total Salary is: " + str(total))
    print("New Slave: " + name + ", go to the basement, NOW!!!")

    bye = input("\nWould you like to Register a New Slave again? (y/n): ")
    if bye.lower() != "y":
        break
print("\n--- Starting a new Registration ---")


    #import time
    #time.sleep(5)

input("\nEnter to Close...")
