# Library
import time
import os

# Clear Terminal 
def clear(): 
    time.sleep(1)
    os.system("clear")
    os.system("cls")

#  Main Menu
def main():
    while True:
        print("=" * 10)
        print("CONQUEST OF STARS")
        print("=" * 10)

        print("[PLAY] Play the Game")
        print("[EXIT] Exit the Game")
        print("=" * 10)

        print("By Nadier Ashemour")
        print("Using Python")
        print("Build Alpha")
        print("=" * 10)

        print("Choose the Menu : ")
        print("=" * 10)

        main_select = input("> ")
        clear()

        if main_select == "PLAY": 
            choose_menu()
        elif main_select == "EXIT":
            break
        else: 
            print("Not Valid!")

# Choose Menu 
def choose_menu():
    while True: 
        print("=" * 10)
        print("WHICH NATION DO YOU WANT TO LEAD?")
        print("=" * 10)
        print("1 - UESCo")
        print("=" * 10)
        print("2 - CLoSIS")
        print("=" * 10)
        print("0 - BACK TO MAIN MENU")
        print("=" * 10)

        choose_select = input("> ")
        print("=" * 10)
        clear()

        if choose_select == "0":
            break
        elif choose_select == "1": 
            desc_uesco()
            break
        elif choose_select == "2": 
            desc_closis()
            break
        else: 
            print("Not Valid!")

# Nation Overview
def desc_uesco(): 
    print("You are playing as the United Earth and the Star Colonies")
    input("Press 'Enter' to return to Main Menu...")
    clear()

def desc_closis(): 
    print("You are playing as Confederation of Lower Sol Independent Systems")
    input("Press 'Enter' to return to Main Menu...")
    clear()

main()