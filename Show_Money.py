import CalcSeparators

def Show_Money():
    userID = int(input("Please enter your user ID: "))
    with open(r"accountfiles.txt","r") as file:
        f = file.readlines()
        if userID > len(f) or userID < 1:
            print("Error: That User ID does not exist")
            return
        details = f[userID-1]
        #This function calculates the positions of the separators in the line of text
        Separators = CalcSeparators.CalcSeparators(details)
        if len(Separators) == 0:
            print("Error: That User ID does not exist")
            return
    print("Your balance is: " , details[Separators[1]+1:Separators[2]]) 