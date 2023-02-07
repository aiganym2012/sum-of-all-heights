# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name11= name1.lower() 
name22= name2.lower() 
true = name11.count("t") + name11.count("r") + name11.count("u") + name11.count("e") + name22.count("t") + name22.count("r") + name22.count("u") + name22.count("e")
love = name11.count("l") + name11.count("o") + name11.count("v") + name11.count("e") + name22.count("l") + name22.count("o") + name22.count("v") + name22.count("e")
z = int(str(true) + str(love))
print(z)

if z<10  or z>90:
  print(f"Your score is {z}, you go together like coke and mentos.")
elif z>40 and z<50:
  print(f"Your score is {z}, you are alright together.")
else:
  print(f"Your score is {z}.")

