# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# TRUE and LOVE
combined_name = (name1 + name2).lower()
# print(combined_name)

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
love = l + o + v + e

love_score = int(str(true)+str(love))
# print(f'Your score is {love_score}.')

if (love_score < 10) or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
