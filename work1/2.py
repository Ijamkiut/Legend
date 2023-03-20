import re

username = input("Please Enter Your Username : ")
passwd = input("Please Enter Your Password : ")
	 
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
reg1 = '^[A-Z]+$'

pat = re.compile(reg)
pat1 = re.compile(reg1)

mat = re.search(pat, passwd)
mat = re.search(pat1, username)
	
if not re.match(reg1, username):
    print("Invalid username! Username must be all alphabetical.")
elif not re.match(reg, passwd):
    print("Invalid password! Password must be at least 7 characters with a digit, special character, and uppercase letter.")
else:
    print("You are logged into the system")