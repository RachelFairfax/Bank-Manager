import time

def login():
    inputuser = input("Please enter your username: ")
    #Check if username is valid
    usernames = []
    # read file
    with open("accountfiles.txt","r") as file:
        f = file.readlines()
        i = 0
        while i < len(f):
            if CalcSeparators(f[i]) == []:
                i += 1
            else:
                Separators = CalcSeparators(f[i])
                usernames.append(f[i][Separators[4]+1:Separators[5]])
                i +=1

        while inputuser not in usernames:
            time.sleep(0.5)
            print("That username does not exist")
            inputuser = input("Please enter your username: ")
        #Get correct password
        index = usernames.index(inputuser)
        passwords = []
        i = 0
        while i < len(f):
            if CalcSeparators(f[i]) == []:
                i += 1
            else:
                Separators = CalcSeparators(f[i])
                passwords.append(f[i][Separators[5]+1:len(f[i])])
                i += 1
        password = passwords[index].strip()
        time.sleep(0.5)
    inputpassword = input("Please enter your password: ")
    while password != inputpassword:
        time.sleep(0.5)
        print("Incorrect password")
        inputpassword = input("Please enter your password: ")
    time.sleep(0.5)
    print("You are now logged in.")
    #Get role
    roles = []
    i = 0
    while i < len(f):
        if CalcSeparators(f[i]) == []:
            i += 1
        else:
            Separators = CalcSeparators(f[i])
            roles.append(f[i][Separators[3]+1:Separators[4]])
            i += 1
    role = roles[index]
    role = role.strip()
    time.sleep(0.5)
    return role

class Account:
    def __init__(self, name, address,balance,ID,role,username,password):
        self.name = name
        self.address = address
        self.balance = balance
        self.ID = ID
        self.role = role
        self.username = username
        self.password = password

    def Add_User():
        file = open("accountfiles.txt","a")
        #Calculates ID using the length of the file
        with open("accountfiles.txt", 'r') as fp:
            count = 1
            for line in enumerate(fp):
                count += 1
            userID = count
        name = input("Please enter your full name: ")
        time.sleep(0.5)
        address = input("Please enter your address: ")
        time.sleep(0.5)
        balance = str(float(input("Please enter the amount of money you would like to deposit: ")))
        time.sleep(0.5)
        role = input("Please enter your role: ")
        while role != "admin" and role != "user":
            time.sleep(0.5)
            print("Not a vaild role")
            role = input("Pleae enter your role: ")
            time.sleep(0.5)
        username = input("Please enter your username: ")

        #Check if username is taken
        usernames = []
        # read file
        with open("accountfiles.txt","r") as file:
            f = file.readlines()
            i = 0
            while i < len(f):
                if CalcSeparators(f[i]) == []:
                    i += 1
                else:
                    Separators = CalcSeparators(f[i])
                    usernames.append(f[i][Separators[4]+1:Separators[5]])
                    i += 1
            while username in usernames:
                time.sleep(0.5)
                print("Sorry, that username is already taken")
                username = input("Please enter your username: ")

        time.sleep(0.5)
        password = input("Please enter your password: ")

        #Checks password is the same
        time.sleep(0.5)
        password1 = input("Please re-renter your password: ")
        while password1 != password:
            print("Passwords do not match")
            password = input("Please enter your password: ")
            time.sleep(0.5)
            password1 = input("Please re-enter your password: ")
        account = Account(name,address,balance,str(userID),role,username,password)

        #Writes details to the file
        file = open("accountfiles.txt","a")
        file.write(account.name+"|"+account.address+"|"+account.balance + "|" + account.ID + "|" + account.role + "|" + account.username + "|" + account.password + "\n")
        time.sleep(0.5)
        print("Your ID is "+str(account.ID))

    def Delete_User():
        userID = int(input("Please enter your user ID: "))
        # list to store file lines
        lines = []
        # read file
        with open("accountfiles.txt", 'r') as fp:
            # read and store all lines into list
            lines = fp.readlines()
            if userID > len(lines) or userID < 1:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            lines[userID-1] = " \n"
        # Write file
        with open("accountfiles.txt", 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                fp.write(line)

    def Show_Money():
        userID = int(input("Please enter your user ID: "))
        with open("accountfiles.txt","r") as file:
            f = file.readlines()
            if userID > len(f) or userID < 1:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            details = f[userID-1]
            #This function calculates the positions of the separators in the line of text
            Separators = CalcSeparators(details)
            if len(Separators) == 0:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
        time.sleep(0.5)
        print("Your balance is: " , details[Separators[1]+1:Separators[2]]) 

    def Show_Address():
        userID = int(input("Please enter your user ID: "))
        with open("accountfiles.txt","r") as file:
            f = file.readlines()
            if userID > len(f) or userID < 1:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            details = f[userID-1]
            #This function calculates the positions of the separators in the line of text
            Separators = CalcSeparators(details)
            if len(Separators) == 0:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
        time.sleep(0.5)
        print("Your address is: " , details[Separators[0]+1:Separators[1]]) 
    
    def Edit_Details():
        input1 = False
        userID = int(input("Please enter your user ID: "))
        with open("accountfiles.txt","r") as file:
            f = file.readlines()
            if userID > len(f) or userID < 1:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            details = f[userID-1]
            #This function calculates the positions of the separators in the line of text
            Separators = CalcSeparators(details)
            if len(Separators) == 0:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            Message = ("Would you like to edit: \n 1. Your name \n 2. Your address \n 3. Quit")
            print(Message)
            while input1 == False:
                time.sleep(0.5)
                answer = input("Please enter your choice: ")
                if answer == "1" or answer == "2" or answer == "3":
                    input1 == True
                    if answer == "1":
                        time.sleep(0.5)
                        name = input("Enter your name: ")
                        details = details.replace(details[0:Separators[0]],name)
                    elif answer == "2":
                        time.sleep(0.5)
                        address = input("Enter your new address: ")
                        details = details.replace(details[Separators[0]+1:Separators[1]],address)
                    else:
                        return
                    f[userID-1] = details
                    #Write changes to file
                    with open("accountfiles.txt", 'w') as fp:
                        # iterate each line
                        for number, line in enumerate(f):
                            fp.write(line)
                else:
                    time.sleep(0.5)
                    print("Incorrect choice. You must enter a number between 1 and 3.")

    def Update_Balance():
        userID = int(input("Please enter your user ID: "))
        with open("accountfiles.txt","r") as file:
            f = file.readlines()
            if userID > len(f) or userID < 1:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            details = f[userID-1]
            #This function calculates the positions of the separators in the line of text
            Separators = CalcSeparators(details)
            if len(Separators) == 0:
                time.sleep(0.5)
                print("Error: That User ID does not exist")
                return
            balance = float(details[Separators[1]+1:Separators[2]])
            time.sleep(0.5)
            print("Your balance is: "+str(balance))
            answer = float(input("Enter the new balance: "))
            balance = answer
            details = details.replace(details[Separators[1]+1:Separators[2]],str(balance))
            print(details)
            f[userID-1] = details
            #Write changes to file
            with open("accountfiles.txt", 'w') as fp:
                # iterate each line
                for number, line in enumerate(f):
                    fp.write(line)

def CalcSeparators(details):
    separators = []
    for index in range (len(details)):
        if details[index] == "|":
            separators.append(index)
    return separators

def Display_Users():
    with open("accountfiles.txt","r") as file:
        f = file.readlines()
        i = 0
        while i < len(f):
            if CalcSeparators(f[i]) == []:
                i += 1
            else:
                Separators = CalcSeparators(f[i])
                print(f[i][0:Separators[0]])
                i += 1
        time.sleep(2)

def More_Money():
    money = float(input("Please enter the minimum amount of money: "))
    time.sleep(0.5)
    with open("accountfiles.txt","r") as file:
        f = file.readlines()
        for i in range (0,len(f)):
            Separators = CalcSeparators(f[i])
            if float(f[i][Separators[1]+1:Separators[2]] ) > money:
                print(f[i][0:Separators[0]])

def Same_Name():
    names = []
    with open("accountfiles.txt","r") as file:
        f = file.readlines()
        i = 0
        while i < len(f):
            if CalcSeparators(f[i]) == []:
                i += 1
            else:
                Separators = CalcSeparators(f[i])
                names.append(f[i][0:Separators[0]])
                i += 1
        time.sleep(0.5)
        print("Users with the same name: ");    
        #Searches for duplicate element    
        for i in range(0, len(names)):    
            for j in range(i+1, len(names)):    
                if(names[i] == names[j]):    
                    print(names[j])    
                    
