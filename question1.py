class PasswordManager:

    def __init__(self,password,entered_pass):
        self.password = password
        self.entered_pass = entered_pass

    def old_passwords(self):
        password = make_as_list[-1]
        return password

    def get_passwords(self):
        print('yysahdsadsadad')
        obj.set_passwords()

    def set_passwords(self):
        if self.entered_pass not in self.password():
            newpass = input('Please enter your new password to reset')
            nm = open('password','a')
            nm.write(f'\n{newpass}')
            nm.close()
            print('You Have reset the password!')

        else:
            print('This password Is already in the system once,Thank you')

    def is_correct(self):
        if self.entered_pass == obj.old_passwords():
            print('You Have Enter The Right Password')
        
        else:
            print('The Password Is Wrong!!')
            obj.get_passwords()

list_of_password = open('password.txt').read()
make_as_list = list_of_password.split()

pas = input('Please Enter Your Password : ')
obj = PasswordManager(make_as_list,pas)
obj.is_correct()
