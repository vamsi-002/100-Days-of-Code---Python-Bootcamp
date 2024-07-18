print('''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("🏝️ Welcome to Treasure Island! 🌴")
print("Your mission is to find the treasure. Make your choices wisely to avoid dangers and reach the treasure!")

print("Chapter 1: The Fork in the Road 🚶‍♂️")
direction = input('You come to a fork in the road. There are two paths. Type "left" or "right": ').lower()

if direction == "left":
    print("Chapter 2: The River Crossing 🌊")
    action = input('You reach a wide, fast-flowing river. Do you "wait" for a boat or "swim" across?: ').lower()
    
    if action == "wait":
        print("You decide to wait by the dock. After a few minutes, a friendly fisherman appears and offers to take you across. You safely reach the other side.")
        print("Chapter 3: The Three Doors 🚪🚪🚪")
        door = input('You come across an ancient stone temple with three doors: one blue, one yellow, and one orange. Which door do you choose? Type "blue", "yellow", or "orange": ').lower()
        
        if door == "blue":
            print("You open the blue door and step inside. The door slams shut behind you, and you hear growls. Wild beasts emerge from the shadows and you have nowhere to run.")
            print("Game Over!!!")
        elif door == "yellow":
            print("You choose the yellow door and enter cautiously. Suddenly, flames erupt from the walls, engulfing the room in fire.")
            print("Game Over!!!")
        elif door == "orange":
            print("You take a deep breath and open the orange door. Inside, you find a room filled with gold and jewels. You’ve found the treasure!")
            print("You Win!!!")
        else:
            print("You encounter unforeseen dangers such as quicksand, poisonous plants, or hidden traps.")
            print("Game Over!!!")
    else:
        print("You dive into the water, but the current is too strong. You’re swept away and attacked by a school of hungry trout.")
        print("Game Over!!!")
else:
    print("You walk cautiously into the dark forest. Suddenly, the ground gives way beneath you, and you fall into a deep hole.")
    print("Game Over!!!")
