import random

print("***********************************************")
print("********WELCOME TO THE CAVEMAN BATTLE**********")
print("***********************************************")

player1_name = input("player 1, what is your name?")

player2_name = input("Player 2, what is your name?")

player1_health = 90
player1_ammo = 55
player1_damage = 33

player2_health = 122
player2_ammo = 52
player2_damage = 22

print("\n" + player1_name + " has " + str(player1_health) + " health " + str(player1_ammo) + " rounds of ammo " + str(player1_damage) + " damage") 
print("\n" + player2_name + " has " + str(player2_health) + " health " + str(player2_ammo) + " rounds of ammo " + str(player2_damage) + " damage") 
 
print('\n Your cave suddenly is attacked by wild animals. What do you do?') 
print('1. Fight') 
print('2. Run') 
print('3. Search for supplies')

choice1 = int(input("Enter either 1,2 or 3 :"))
choice2 = int(input("Enter either 1,2 or 3 :"))

if choice1 == 1: 
    print('\n '+ player1_name + ' decides to fight the intruders and does ' + str(player1_damage)+ " damage per shot! ")
    player1_ammo -= 10
    if player1_ammo < 0:
        print("\n" + player1_name + ' decides to fight the intruders and does ' + str(player1_damage)+ " damage per shot! ") 
    player1_ammo -= 10 
    if player1_ammo > 0: 
        print('\n ' + player1_name + ' defeated the animals!! They have' + str(player1_ammo) + " rounds of ammo left ") 
elif choice1 == 2: 
    print('lived to fight another day') 
elif choice1 == 3: 
    random_number = random.randint(1,10) 
    print(random_number) 
    if random_number <= 5: 
        print("the manage to save some foods") 
    else: 
        print("they manage to ran away with their cloths")

    print('the animals manage to chase them out') 
    print("But Sundenly The boar Bite Player 1 And it deal 20 damage to player 1 ")
    player2_health -= 20
else: 
    print('Invalid input, sad day for the caveman')

print( "\n"+"-----------------------------------------------------------")

if choice2 == 1: 
    print('\n '+ player2_name + ' decides to fight the intruders and does ' + str(player2_damage)+ " damage per shot! ")
    player2_ammo -= 10
    if player2_ammo < 0:
        print("\n" + player2_name + ' decides to fight the intruders and does ' + str(player2_damage)+ " damage per shot! ") 
    player2_ammo -= 10 
    if player2_ammo > 0: 
        print('\n ' + player2_name + ' defeated the animals!! They have' + str(player2_ammo) + " rounds of ammo left ") 
elif choice2 == 2: 
    print('lived to fight another day') 
elif choice2 == 3: 
    random_number = random.randint(1,10) 
    print(random_number) 
    if random_number <= 5: 
        print("the manage to save some foods") 
    else: 
        print("they manage to ran away with their cloths")

    print('the animals manage to chase them out') 
    print("But Sundenly The boar Bite Player 2 And it deal 20 damage to player 2 ")
    player2_health -= 20
else: 
    print('Invalid input, sad day for the caveman')

print( "\n"+"-----------------------------------------------------------")

print("Player 1 Name : " + player1_name)
print("Player 1 Health : " + str(player1_health))
print("Player 2 Name : " + player2_name)
print("Player 2 Health : " + str(player2_health))