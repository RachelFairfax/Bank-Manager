import CalcSeparators

def Display_Users():
    with open(r"accountfiles.txt","r") as file:
        f = file.readlines()
        for i in range (0,len(f)-1):
            Separators = CalcSeparators.CalcSeparators(f[i])
            print()
