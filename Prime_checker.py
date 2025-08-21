# Prime Checker

def Prime_Checker(n):
    a = 2
    p = True

    while n > a:
        if n % a == 0:
            p = False
            break
        a = a + 1
    return p

while True:
    n = int(input("Enter Your Number: "))
    #q = Prime_Checker(n)  # Call the Prime_Checker function and assign its return value to p

    if Prime_Checker(n):  # Call the function with the input n
        print("Prime")
    else:
        print("Not Prime")

    q = input("Do you want to repeat_(Y/N): ").lower()
    if q != "y":
        break

input("\nEnter to Close...")