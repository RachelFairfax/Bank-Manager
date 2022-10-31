import CalcSeparators

def Edit_Details():
    input1 = False
    userID = int(input("Please enter your user ID: "))
    with open(r"accountfiles.txt","r") as file:
        f = file.readlines()
        if userID > len(f) or userID < 1:
            print("Error: That User ID does not exist")
            return
        details = f[userID-1]
        #This function calculates the positions of the separators in the line of text
        Separators = CalcSeparators.CalcSeparators(userID,details)
        if len(Separators) == 0:
            print("Error: That User ID does not exist")
            return
        Message = ("Would you like to edit: \n 1. Your name \n 2. Your address \n 3. Quit")
        print(Message)
        while input1 == False:
            answer = input("Please enter your choice: ")
            if answer == "1" or answer == "2" or answer == "3":
                input1 == True
                if answer == "1":
                    name = input("Enter your name: ")
                    details = details.replace(details[0:Separators[0]],name)
                elif answer == "2":
                    address = input("Enter your new address: ")
                    details = details.replace(details[Separators[0]+1:Separators[1]],address)
                else:
                    return
                f[userID-1] = details
                #Write changes to file
                with open(r"accountfiles.txt", 'w') as fp:
                    # iterate each line
                    for number, line in enumerate(f):
                        fp.write(line)
            else:
                print("Incorrect choice. You must enter a number between 1 and 3.")