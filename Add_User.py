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