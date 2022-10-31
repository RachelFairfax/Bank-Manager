import CalcSeparators

def Update_Balance():
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
        Balance = float(details[Separators[1]+1:Separators[2]])
        print("Your balance is: "+str(Balance))
        answer = float(input("Enter the new balance: "))
        Balance = answer
        details = details.replace(details[Separators[1]+1:Separators[2]],str(Balance))
        print(details)
        f[userID-1] = details
        #Write changes to file
        with open(r"accountfiles.txt", 'w') as fp:
            # iterate each line
            for number, line in enumerate(f):
                fp.write(line)