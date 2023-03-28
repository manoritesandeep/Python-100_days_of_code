"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.
"""

def prime_calc(number):   
    for i in range(2,number):
        if (number % i)==0:
            # Not a prime
            print("It's not a prime number.")
            break
    # If above if statement doesn't trigger that means Number is prime
    else:
        print("It's a prime number.")       

prime_calc(9)
prime_calc(7)

#### Using a randomly generated number ####

import random as r
random_num = r.choice(list(range(0,100)))
print(random_num)
# Take this random number and check for prime:
for i in range(2,random_num):
    if random_num%i == 0:
        print(f"{random_num} is not a prime number.")
        break
else:
    print(f"{random_num} is a prime number.")