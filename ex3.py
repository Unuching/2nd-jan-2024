import random


names = input("Give me all of your names separated by comma.")

name_list = names.split(", ")

r_name = random.choice(name_list)

print(r_name + " is going to pay today!")