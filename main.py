import os

console_input = ""

def print_menu():
    print("middle grip - 0")
    print("right grip - 1")
    print("left grip - 2")
    print("all of the above - 3")
    print("")
    print("write \"use\" followed by an option number")
    print("")

def print_help():
    pass

print_menu()

while True:
    console_input = input("BCLU >").lower()

    if(console_input == "exit" or console_input == "quit"):
        os._exit(0)

    if(console_input == "menu"):
        print_menu()

    if(console_input == "help"):
        print_help()

    if(console_input.startswith("use")):
        option = console_input[4:]

        if(option == "0"):
            print("=000")

    
