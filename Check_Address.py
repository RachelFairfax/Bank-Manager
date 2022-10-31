import CalcSeparators

def Show_Address():
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
    print("Your address is: " , details[Separators[0]+1:Separators[1]]) 