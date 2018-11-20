 #!/bin/python3

items = [
"A: 3 litres of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: A 10 day oxygen supply",
"F: Solar panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 3 day food supply"
]

print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
print("You can get to the base in 3 days on your lunar rover")
print("The lunar rover can only fit you in your spacesuit and 4 other items")
print("Out of the items below, which do you bring? \n")

for objects in items:
    print(objects)

print("Pick the first most import items for survival")
user_choice = input(">>> ")

user_list =  list(user_choice.split(','))
print(user_list)


if "A" not in user_list:
  print("no water => no live Rule1 of the Universe")

if "E" not in user_list:
  print("You need Oxygen You foool")

if "F" not in user_list:
  print("No Engergy ==> no Vehicle movemnt ==> you die")

if "I" not in user_list:
  print("Because of great hunger and dizzyness you drive off into a cliff you need food to drive")

#Tells user whether or not they will make it safely
if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
  print("Boooya you got there safe")
else:
  print("First human to die on mars achievement!")