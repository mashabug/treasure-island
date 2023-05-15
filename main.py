treasure = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_question = input("It has been raining the whole night so today there is fog and you cannot see anything.\nYou need to listen to your intuition and choose where to go: left or right?\n").lower()

if first_question == "left":
  print("Great job! You have a very good intuition!\nYou are one step closer to the treasure!")
  second_question = input("You need to cross the river but you see trout are spawning. What do you want to do: swim or wait?\n ").lower()
  
  if second_question == "wait":
    print("Yay! You almost found the treasure!")
    third_question = input("You see three doors in front of you. Behind one of them is the treasure! Which door you choose? Red, Yellow or Blue?\n").lower()
    if third_question == "yellow":
      print("CONGRATULATIONS! YOU FOUND THE TREASURE!")
      print(treasure)
    elif third_question == "blue":
      print("Wrong door! You have been eaten by beasts. Game over.")
    else:
      print("Danger! There is fire! You burned! Game over.")
  else:
    print("Oh no! You attacked by trout! Game over.")
  
else:
  print("Oops... You fell into the hole. Game over.")
