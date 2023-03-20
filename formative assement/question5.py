password = '1234_naqiu'
max_attempt = 5
i = 0

while i < max_attempt:
    guess = input('Please enter your Password : ')
    i = i + 1
    if guess == password:
        print('you are log into the system')
        break
else:
        print('you are blocked into the system') 
