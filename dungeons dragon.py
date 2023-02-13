print("""

  _____                                                    _____                              
 |  __ \                                           ___    |  __ \                             
 | |  | |_   _ _ __   __ _  ___  ___  _ __  ___   ( _ )   | |  | |_ __ __ _  __ _  ___  _ __  
 | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|  / _ \/\ | |  | | '__/ _` |/ _` |/ _ \| '_ \ 
 | |__| | |_| | | | | (_| |  __/ (_) | | | \__ \ | (_>  < | |__| | | | (_| | (_| | (_) | | | |
 |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|___/  \___/\/ |_____/|_|  \__,_|\__, |\___/|_| |_|
                      __/ |                                                  __/ |            
                     |___/                                                  |___/             

""")
print("welcome to Dungeons & Dragon ")

Player_name = input("What is Your Name : ")

health = 100
damage = 20 

print("\welcome, " + Player_name + "You Have :" + str(health) + "health and can do damage " + str(damage))
print("You Came Accros a Dragon!! what will you do??")
print("1.Fight")
print("2.Run")

choice = int(input("Enter either 1 or 2 :"))
if choice == 1:
    print("You attack the dragon and do " + str(damage) + ' damage') 
    print('the dragon back off, spit some acid and does 10 damage') 
    health -= 10 
    print('Your current health is ' + str(health)) 
    print("---------------------------------------------------------------------------------------------------------")
    print("after the dragon run away....")
    print("you will have a choice to : ")
    print("1.Save Princess")
    print("2.ignore Princess")
    choice = int(input("Enter either 1 or 2 :"))
    if choice == 1:
        print("The Princess Happy......")
        print("The Princess Will marry You....")
        print("And happily aver after")
    else:
        print("The princess will mad at you....")

elif choice == 2:
    print('You run away from the dragon') 
    print('live today for tomorrow') 
    print("But The dragon sudenly throw a rock and manage to hit you,it will deals double damage to you")
    health -= (10*2)
    print("Your current health : " + str(health))

else:
    print("\Invalid choice, the dragon get to eat you alive!! ")
    print("thanks for playing")
