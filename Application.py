import Utils

INVALID_CHOICE_MESSAGE = "Invalid response. Try again."
RUN_AGAIN_MESSAGE = "Would you like to try another option? Type YES or NO: "
MENU_MESSAGE =  "\n How can we help you today? \n " \
                "1. Add user \n " \
                "2. Delete user \n " \
                "3. Check balance \n " \
                "4. Show address \n " \
                "5. Edit details \n " \
                "6. Update balance \n " \
                "7. Output all users with the same name \n " \
                "8. Get all users with more money than a given amount \n " \
                "9. Display all users \n" \
                "10. Quit \n"
WELCOME_MESSAGE = "WELCOME TO OUR BANKING APP "
INPUT_CHOICE_MESSAGE = "Please enter your choice (between 1 and 9): "
GOODBYE_MESSAGE = "We are sorry to see you go. \n Have a nice day :)"

    
def menu():

    while True:
        print(MENU_MESSAGE)
        choice = input(INPUT_CHOICE_MESSAGE)
        if choice == '1':
            Utils.Add_User()
        elif choice == '2':
            Utils.Delete_User()
        elif choice == '3':
            Utils.Show_Money()
        elif choice == '4':
            Utils.Show_Address()
        elif choice == '5':
            Utils.Edit_Details()
        elif choice == '6':
            Utils.Update_Balance()
        elif choice == '7':
            Utils.Same_Name()
        elif choice == '8':
            Utils.More_Money()
        elif choice == '9':
            Utils.Display_Users()
        elif choice == '10':
            print(GOODBYE_MESSAGE)
            break
        else:
            print(INVALID_CHOICE_MESSAGE)

def main():
    print(WELCOME_MESSAGE)
    menu()

main()