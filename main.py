import os
from time import sleep
import customer as c

with open("data.txt", encoding="utf-8", mode="r") as file:
    data = file.readlines()
    osoba = [c.Customer] * (len(data)+1)
    for i in range(len(data)):
        info = (data[i]).split(":")
        osoba[i] = c.Customer(str(info[0]),str(info[1]),int(info[2]),float(info[3]))

while True:
    os.system("CLS")
    option = str(input("Type \'L\' for login or \'C\' for creating account or \'Q\' for quit: "))

    if option == "L" or option == "l":
        os.system("CLS")
        print("=-=-=-=-LOGGING PAGE-=-=-=-=\n")
        l = str(input("Enter your login: "))
        p = str(input("Enter your password: "))
            
        with open("data.txt", encoding="utf-8", mode="r") as file:
                temp_data = file.readlines()
                temp_logins = [""] * len(temp_data)
                temp_passwords = [""] * len(temp_data)
                for i in range(len(temp_logins)):
                    temp_logins[i] = (temp_data[i].split(":"))[0]
                    temp_passwords[i] = (temp_data[i].split(":"))[1]
        f = False
        for j in range(len(temp_data)):
            if l.capitalize() == temp_logins[j].capitalize():
                f = True
                break
            else:
                f = False

        if not f:
            print("\nAccount with that login doesnt exist. You can create one if you want.")
            sleep(2)
        else:
            for j in range(len(temp_data)):
                if l.capitalize() == temp_logins[j].capitalize():
                    if(p==temp_passwords[j]):
                        index = j
                        pa = True
                        break
                    else:
                        pa = False

            if not pa:
                print("\nERROR: Password is incorrect!")
                sleep(2)
            else:
                print("\nPassword is correct!")
                print("In few seconds you will be directed to account page!")
                sleep(3)

                while True:
                    os.system("CLS")

                    user = osoba[index]

                    print("YOUR ACCOUNT\n")
                    print("1) Balance")
                    print("2) Deposit")
                    print("3) Withdraw")
                    print("4) Your login and password")
                    print("5) Your ID")
                    print("6) Logout")
                    print("7) Delete account")
                    print("8) Quit\n")

                    pos = int(input("Choose between 1-8: "))

                    match pos:
                        case 1:
                            print("\nYour balance is: $" + str(user.balance()))
                            input()
                        case 2:
                            amount = float(input("How much money do you want deposit: "))
                            user.deposit(amount)
                            print("\nYou've successfully deposited $" + str(amount))
                            input()
                        case 3:
                            amount = float(input("How much money do you want to withdraw: "))
                            if(user.withdraw(amount)):
                                print("\nYou've successfully withdrawed $" + str(amount))
                                input("")
                            else:
                                print("\nYou dont have enough money!")
                                input("")
                        case 4:
                            print("\nYour login is: " + str(user.login))
                            print("Your password is: " + str(user.password))
                            input("")
                        case 5:
                            print("\nYour account's ID is: " + str(user.id))
                            input("")
                        case 6:
                            print("\nLogging out...")
                            sleep(3)
                            print("\nYou've been successfully logged out! Goodbye!")
                            sleep(1)
                            break
                        case 7:
                            ans = str(input("\nAre you sure you want to delete your account?(Y,N): "))
                            if ans == "Y" or ans == "y":
                                pass
                                temp_pas = str(input("\nTo delete your account you need to provide your current password: "))
                                if temp_pas == temp_passwords[index]:
                                    #deleting account
                                    osoba[index].to_delete()
                                    del osoba[index]
                                    del temp_data[index]
                                    del temp_logins[index]
                                    del temp_passwords[index]

                                    print("\nDeleting your account...")
                                    sleep(4)
                                    print("Your account has been deleted!")
                                    print("Logging out...")
                                    sleep(2)
                                    break
                                else:
                                    print("\nERROR: Password is incorrect!")
                                    print("Cancelling...")
                                    sleep(2)
                            
                            if ans == "N" or ans == "n":
                                print("\nCancelling...")
                                sleep(2)
                                
                        case 8:
                            print("\nGoodbye!")
                            sleep(2)
                            exit()

    if option == "C" or option == "c":
        while True:
            os.system("CLS")
            print("=-=-=-=-ACCOUNT CREATOR-=-=-=-=\n")

            l = str(input("Enter your new login: "))
            p = str(input("Enter your new password: "))
            id = c.new_id_creator()
            b = 0.0

            with open("data.txt", encoding="utf-8", mode="r") as file:
                temp_logins = file.readlines()
                for i in range(len(temp_logins)):
                    temp_logins[i] = (temp_logins[i].split(":"))[0]

            con = False
            for j in range(len(temp_logins)):
                if l.capitalize() == temp_logins[j].capitalize():
                    print("\nERROR: This login is not available. Try another.")
                    sleep(2)
                    con = True
                    break
                con = False

            if not con:
                if len(temp_logins) == 0:
                    con = True
                break
   
        print("\nYour login: " + str(l) + "\nYour password: " + str(p) + "\nYour ID: " + str(id) + "\nYour balance: " + str(b))
        input("\nIf the information above is good, press ENTER.")
        print("\nCreating account...")
        sleep(3.5)
        print("\nYour account was successfully created!")
        print("In few seconds you will be directed to login page!")

        osoba.append(c.Customer(l,p,id,b))
        sleep(3)

    if option == "Q" or option == "q":
        break





