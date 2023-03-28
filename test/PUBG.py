from PUBGdetails import player,enemy

Red = "\u001b[31m"
black = "\u001b[30m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
reset = "\033[1;0m"

print(black + "**************************************************************")
print(black + "**********************"+ Cyan +"WELCOME TO PUBG"+ black +"*************************" + reset)
print(black + "**************************************************************" + reset)

nama1 = input("Please Enter Your Nama : ")
id1 = input("Please Enter Your Id : ")

Player = player(nama1,id1,100,100)
Enemy = enemy('Jamal',123123123,100,100)

Player.introduction1()
