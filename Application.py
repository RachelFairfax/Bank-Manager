import Utils as A

def main():
    Quit = False
    print("WELCOME TO OUR BANKING APP \n \n")
    while Quit == False:
        Quit = menu()
    print("\n")
    print("We are sorry to see you go. Have a nice day :)")
    
def menu():
    INVALID_CHOICE_MESSAGE = "Invalid response. Try again."
    RUN_AGAIN_MESSAGE = "Would you like to try another option? Type YES or NO: "
    print("How can we help you today? \n")
    print("1. Add user")
    print("2. Delete user")
    print("3. Check balance")
    print("4. Show address")
    print("5. Edit details")
    print("6. Update balance")
    print("7. Output all users with the same name")
    print("8. Get all users with more money than a given amount")
    print("9. Display all users \n")

    choice = int(input("Please enter your choice (between 1 and 9): "))
    while choice < 1 or choice > 9:
        print(INVALID_CHOICE_MESSAGE)
        choice = input("Please enter your choice: ")
    if choice == 1:
        A.Add_User()
    elif choice == 2:
        A.Delete_User()
    elif choice == 3:
        A.Show_Money()
    elif choice == 4:
        A.Show_Address()
    elif choice == 5:
        A.Edit_Details()
    elif choice == 6:
        A.Update_Balance()
    elif choice == 7:
        A.Same_Name()
    elif choice == 8:
        A.More_Money()
    elif choice == 9:
        A.Display_Users()

    run_again = input(RUN_AGAIN_MESSAGE)
    while run_again != "YES" and run_again != "NO":
        print(INVALID_CHOICE_MESSAGE)
        run_again = input(RUN_AGAIN_MESSAGE)
    if run_again == "YES":
        return False
    else:
        return True

main()