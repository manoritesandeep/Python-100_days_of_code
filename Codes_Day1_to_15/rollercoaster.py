print("Welcome to the rollercoaster")
height = int(input("What is your height?"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age<12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age<=18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age>=45 and age<=55:
        print("Everything is going to be alright. Have a free ride on us!")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        bill += 3
    
    print(f"Your total is ${bill}.")

else:
    print("Sorry, you do not meet the height requirements")

