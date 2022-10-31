import Add_User as A
import Delete_User as B
import Check_Balance as C
import Check_Address as D
import Edit_Details as E
import Update_Balance as F
import Same_Name as G
import More_Money as H
import Show_Money as I

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
    print("8. Get all users with more money than a given amount")
    print("9. Display Balance \n")

    choice = int(input("Please enter your choice: "))
    while choice < 1 or choice > 9:
        print("Invalid choice, enter a number between 1 and 8.")
        choice = input("Please enter your choice: ")
    if choice == 1:
        A.Add_User()
    elif choice == 2:
        B.Delete_User()
    elif choice == 3:
        C.Check_Balance()
    elif choice == 4:
        D.Show_Address()
    elif choice == 5:
        E.Edit_Details()
    elif choice == 6:
        F.Update_Balance()
    elif choice == 7:
        G.Same_Name()
    elif choice == 8:
        H.More_Money()
    elif choice == 9:
        I.Show_Money()

    run_again = input("Would you like to try another option? Type YES or NO: ")
    while run_again != "YES" and run_again != "NO":
        print("Invalid response. Try again.")
        run_again = input("Would you like to try another option? Type YES or NO: ")
    if run_again == "YES":
        return False
    else:
        return True

main()