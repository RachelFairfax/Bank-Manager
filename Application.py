import Utils
import pymongo
import time

INVALID_CHOICE_MESSAGE = "Invalid response. Try again."
RUN_AGAIN_MESSAGE = "Would you like to try another option? Type YES or NO: "
ADMIN_MENU_MESSAGE =  "\n How can we help you today? \n " \
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
USER_MENU_MESSAGE = "\n How can we help you today? \n " \
                "1. Add user \n " \
                "2. Check balance \n " \
                "3. Show address \n " \
                "4. Edit details \n " \
                "5. Update balance \n " \
                "6. Quit \n"
WELCOME_MESSAGE = "WELCOME TO OUR BANKING APP "
INPUT_CHOICE_MESSAGE = "Please enter your choice (a number): "
GOODBYE_MESSAGE = "We are sorry to see you go. \n Have a nice day :)"


def menu():
    
    role = Utils.login()
    print("Welcome " + role)
    while True:
        if role == "admin":
            print(ADMIN_MENU_MESSAGE)
            time.sleep(0.5)
            choice = input(INPUT_CHOICE_MESSAGE)
            if choice == '1':
                Utils.Account.Add_User()
            elif choice == '2':
                Utils.Account.Delete_User()
            elif choice == '3':
                Utils.Account.Show_Money()
            elif choice == '4':
                Utils.Account.Show_Address()
            elif choice == '5':
                Utils.Account.Edit_Details()
            elif choice == '6':
                Utils.Account.Update_Balance()
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
        else:
            print(USER_MENU_MESSAGE)
            time.sleep(0.5)
            choice = input(INPUT_CHOICE_MESSAGE)
            if choice == '1':
                Utils.Account.Add_User()
            elif choice == '2':
                Utils.Account.Show_Money()
            elif choice == '3':
                Utils.Account.Show_Address()
            elif choice == '4':
                Utils.Account.Edit_Details()
            elif choice == '5':
                Utils.Account.Update_Balance()
            elif choice == '6':
                time.sleep(0.5)
                print(GOODBYE_MESSAGE)
                break
            else:
                time.sleep(0.5)
                print(INVALID_CHOICE_MESSAGE)


def main():
    print(WELCOME_MESSAGE,"\n")
    menu()

main()