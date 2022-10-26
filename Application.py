

class Account:
    def __init__(self, name, address,balance,ID):
        self.name = name
        self.address = address
        self.balance = balance
        self.ID = ID


def main():
    Quit = False
    print("WELCOME TO OUR BANKING APP \n \n")
    while Quit == False:
        Quit = menu()
    print("\n")
    print("We are sorry to see you go. Have a nice day :)")
    

def menu():
    print("How can we help you today? \n")
    print("1. Add user")
    print("2. Delete user")
    print("3. Check balance")
    print("4. Show address")
    print("5. Edit details")
    print("6. Update balance")
    print("7. Output all users with the same name")
    print("8. Get all users with more money than a given amount \n")

    choice = int(input("Please enter your choice: "))
    while choice < 1 or choice > 8:
        print("Invalid choice, enter a number between 1 and 8.")
        choice = input("Please enter your choice: ")
    if choice == 1:
        Add_User()
    elif choice == 2:
        Delete_User()
    elif choice == 3:
        Check_Balance()
    elif choice == 4:
        Show_Address()
    elif choice == 5:
        Edit_Details()
    elif choice == 6:
        Update_Balance()
    elif choice == 7:
        Same_Name()
    else:
        More_Money()

    run_again = input("Would you like to try another option? Type YES or NO: ")
    while run_again != "YES" and run_again != "NO":
        print("Invalid response. Try again.")
        run_again = input("Would you like to try another option? Type YES or NO: ")
    if run_again == "YES":
        return False
    else:
        return True


def Add_User():
    file = open("accountfiles.txt","a")
    #Calculates ID using the length of the file
    with open(r"accountfiles.txt", 'r') as fp:
        count = 1
        for line in enumerate(fp):
            count += 1
        userID = count
    account = Account(input("Please enter your full name:"),input("Please enter your address: "),input("Please enter the amount of money you would like to deposit: "),str(userID))
    #Writes details to the file
    file = open("accountfiles.txt","a")
    file.write(account.name+"|"+account.address+"|"+account.balance + "|" + account.ID + "\n")
    print("Your ID is "+str(account.ID))

def Delete_User():
    userID = int(input("Please enter your user ID: "))
    # list to store file lines
    lines = []
    # read file
    with open(r"accountfiles.txt", 'r') as fp:
        # read and store all lines into list
        lines = fp.readlines()
        lines[userID-1] = " \n"
    # Write file
    with open(r"accountfiles.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            fp.write(line)


def Check_Balance():
    userID = int(input("Please enter your user ID: "))
    with open(r"accountfiles.txt","r") as file:
        f = file.readlines()
        if userID > len(f) or userID < 1:
            print("Error: That User ID does not exist")
            return
        details = f[userID-1]
        #This function calculates the positions of the separators in the line of text
        Separators = CalcSeparators(userID,details)
        if len(Separators) == 0:
            print("Error: That User ID does not exist")
            return
    print("Your balance is: " , details[Separators[1]+1:Separators[2]]) 

def Show_Address():
    pass

def Edit_Details():
    pass

def Update_Balance():
    pass

def Same_Name():
    pass

def More_Money():
    pass

def CalcSeparators(userID,details):
    separators = []
    for index in range (len(details)):
        if details[index] == "|":
            separators.append(index)
    return separators

main()