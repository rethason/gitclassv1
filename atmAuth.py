
#Initializing the system
import random
from datetime import date 
database = {} #dictionary
today = date.today()
amount= 500

def init():
    print("Welcome to bankPHP"+' ' +"Today's date is :",today )
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()
#login
def login():
    print("Today's date is :", today)
    # - account number & password
    print("********* Please Login Here ***********")
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
    print('Invalid account or password')
    logout()
    

 # - Register  for a new account  number & password
def register():

    print("****** Please Register with us *******")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("Please enter valid email address? \n")
    password = input("Please enter a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
#bank operations
def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1)deposit (2)withdrawal (3)Complaint (4)Logout (5)Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
        login()
    elif(selectedOption == 2):
        
        withdrawalOperation()
        login()
    elif (selectionOption == 3):
         complaint() 
         login()

    elif(selectedOption == 4):
        logout()
    
    elif (selectionOption == 5):
         exit()

    else: 
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    withdraw = int(input ("How much would you like to withdraw \n"))
    print("You entered  %d" % withdraw)
    print("Your  balance is now :")
    print(amount - withdraw)


def depositOperation():
    deposite= int(input ("How much would you like to Depoite \n"))
    print("You entered  %d" % deposite )
    print("Your  balance is is now :")
    print(amount + deposite)
    
def complaint():    
    comp = input ("Please enter complaint here \n")
    print(comp)
    login()

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()
#### ACTUAL BANKING SYSTEM #####
init()
