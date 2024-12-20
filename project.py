#define a dictionary to store user credentials
users={}

def display_menu():
    print("\n---login system--")
    print('1.Register')
    print('2.login')
    print('3.change the password')
    print('4.Exit')
    return input('choose an option (1-4):')

#Register a new user
def register_user():
    username=input('enter a username:')
    if username in users:
        print('username already exists! please choose a differ username.')
    else:
        password=input('enter the password:')
        users[username]=password
        print(f"user '{username}registered successfully!")



#login an existing user
def login_user():
    username=input('enter your username:')
    if username in users:
        password=input('enter your password')
        if users[username]==password:
            print(f'welcome,{username}! you are successfully logged in.')
        else:
            print('incorrect password! please try again.')
    else:
        print('username not found! please register first')

def change_password():
    username=input('enter your username:')
    if username in users:
        old_password=input('enter your current password:')
        if users[username]==old_password:
            new_password=input('enter your new password:')
            users[username]=new_password
            print('password changed successfully')
        else:
            print('current password is incorrect! please try again')
    else:
        print('username not found! please register first.')


while True:
    choice=display_menu()

    if choice=='1':
        register_user()
    elif choice=='2':
        login_user()
    elif choice=='3':
        change_password()
    elif choice=='4':
        print('exiting the login system.Goodbye!')
        break
    else:
        print('invalid choice! please choose a valid option.')

