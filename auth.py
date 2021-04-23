
# Initializing the system
import random
import validation
import database
from getpass import getpass

def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login(user_account_number=None):
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()
        database.create(user_account_number, [first_name, last_name, email, password])

def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, [first_name, last_name, email, password, 0])

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()
        database.create(user_account_number, [first_name, last_name, email, password])


    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    initial_balance = 500;
    withdrawal_amount= float(input("Please Enter amount to be withdraw: "))
    print("You Entered:", withdrawal_amount)

    if withdrawal_amount >  initial_balance :
        print("Insufficient balance:Please enter an another amount")
        withdrawal_operation()
    elif:
        initial_balance <= withdrawal_amount
        balance = withdrawal_amount - initial_balance

    print("Your Current balance is :", balance)
        f = open("wk5/user_record/" + balance  + ".txt", "x")
        f.write(balance);
        f.close();

def deposit_operation():
       initial_balance =0;

       deposit_amount= float(input("Enter amount to be deposited: "))
       print("You Deposited:", deposit_amount)
       balance = deposit_amount + initial_balance
       print("Your Current balnace is  Amount Deposited:", balance )

        f = open("wk5/user_record/" + balance + ".txt", "x")
        f.write(balance);
        f.close();
def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    read(user_account_number)
    database.delete(user_account_number)


init()