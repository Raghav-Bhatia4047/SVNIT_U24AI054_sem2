class Password_manager:
    def __init__(self):
        self.oldpassword=[]
     
    def get_password(self):
        if self.oldpassword:
            return self.oldpassword[-1]
        else:
            return None
    def set_password(self,new_password):
        if(new_password not in self.oldpassword):
            self.oldpassword.append(new_password)
        else:
            print("password must be different")
    def is_correct(self,password):
        return password==self.get_password()
def menu():
    print("""Enter 
         'set' to set password
         'get' to get password
         'check' to check password""")
def main():
    print("Enter '1' to continue '0' to exit" )
password=Password_manager()
while(1):
    main()
    a=int(input())
    menu()
    choice=input()
    match(a):
         case 1:
            match(choice):
                case 'set': 
                    Password=input("enter password:")
                    password.set_password(Password)
                case 'get':
                    password.get_password()
                case 'check':
                    check=input("Enter password:")
                    password.is_correct(check)
         case 0: exit