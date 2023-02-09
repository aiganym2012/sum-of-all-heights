# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
sum=random.randint(0, len(names))
who=names[sum]
print(f"{who} is going to buy the meal today!" )
