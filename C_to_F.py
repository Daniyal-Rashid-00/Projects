while True:
    a = int(input("Do you want to convert (1)Celcious to Faranhight or (2)the other way around (1/2): "))

    if a == 1:
        c = float(input("\nEnter Value in Celcious: "))
        f = (9/5)*c+32
        print(f"\nYour converted Value in Faranhight is: {f}")
    elif a == 2:
        f2 = float(input("\nEnter Value in Faranhight: "))
        c2 = (f2-32) * 5/9
        print("\nYour converted Value in Celcious is: "+ str(c2))
    b = input("\nWould you like to repeat? (y/n)\n").lower()
    
    if b != "y":
        break
input("\nEnter to Close...")