
"""
Created on Fri Sep 16 21:39:07 2022

Guvi Task 1
Name: Vigneshwaran M
Batch : D42
Email: vicky12799@gmail.com
"""
import re;

def register():
    username = validateUsername(input("Enter your username: ").lower().strip())
    
    while True:
        password=input("Enter your password: ")
        if validatePassword(password):
            break;
    db = open('database.txt','a')
    db.write("\n"+username+','+password)
    db.close()
    print("Registration Successful")
    print("Redirecting to login page")
    login(username,password)
      

def validateUsername(username):
    regex = r'\b[A-Za-z][A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    data = database()
    if username not in data:
        if re.fullmatch(regex, username):
            return username
        else:
            print('please enter a valid email address')
            register()
    else:
        print('Username already exists. Please enter unique username')
        register()
        

def validatePassword(password):
      
    specialChar =['$', '@', '#', '%']
    val = True
      
    if len(password) < 5:
        print('length should have min. 5 characters ')
        val = False
          
    if len(password) > 16:
        print('length should be not be greater than 15')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in specialChar for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
        
def login(username=None,password=None):
    username = input("Enter your username: ").lower().strip() if username==None else username
    password = input("Enter your password: ") if password==None else password
    data = database()
    if username in data:
        if data[username].strip()==password:
            print("Logging in... please wait.")
            print('login success')
            pass
        else:
            print("wrong password")
            option = input('retry | forgot password: ')
            if option.lower()=='retry':
                login(username)
            elif option.lower()=='forgot password':
                forgotPassword(username,data)
            else:
                print("Enter valid input")
                login(username,password)
    else:
        print("user doesn't exist try again or register")
        option2 = input("Retry | Register: ")
        if option2.lower()=='retry':
            login()
        elif option.lower()=='register':
            register()
        else:
            print("Enter valid input")
            
    


def forgotPassword(username=None,data= None):
    username = input("Enter your username: ") if username==None else username
    data = database() if data==None else data
    
    option = input("1. Enter 1 to retrieve old password \n2. Enter 2 to change password\n")
    
    if option =="1":
        print("Your old password is " +data[username])
    elif option=="2":
        changePassword(data,username)
    

def changePassword(data,username):
    while True:
        newPassword=input("Enter your new password: ")
        if validatePassword(newPassword):
            break;
    searchText = username+','+data[username]
    replaceText = username+','+newPassword
    
    with open('database.txt','r') as file:
        filedata = file.read()
    filedata = filedata.replace(searchText,replaceText)

    with open('database.txt','w') as file:
        file.write(filedata)
    
    print("Password changed successfully")
    print("Redirecting to login page")
    print('username: '+username)
    login(username)
    
    
def database():
    db = open('database.txt','r')
    d = []
    f = []
    
    for i in db:
        if ',' in i:
            a,b = i.split(',')
            a = a.strip()
            b = b.strip()
            d.append(a)
            f.append(b)   
    data = dict(zip(d,f))
    return data


def homepage(option=None):
    
    option = input("Login | Register: ")
    
    if option.lower().strip() == "login":
        login()
    elif option.lower().strip()=="register":
        register()
    else:
        print("please enter a valid option")
        homepage()
    
print("Please enter an option\n")
homepage()


