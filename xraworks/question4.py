number = 7
attempt = 3
i = 0

while i < attempt:
    guess = int(input("Please enter a number: "))
    i = i + 1 
    if guess == number:
        print("You Win!")
        break
else:
        print("You Lost!")