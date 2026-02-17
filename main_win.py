import sys

def main_win(change_win):
    
    print("\nThis is main window")
    print("Options that you can do:")
    print("- active")
    print("- done")
    print("- create")
    print("- exit\n")


    while True:
        print("Enter your action")
        action = input("> ").lower()

        if action == "active":
            return change_win("list") # Викно списку таскыв з фыльтром
        elif action == "done":
            return change_win("list") # выкно списку завдань з фыльтром
        elif action == "create":
            return change_win("list") # выкно створення таску
        elif action == "exit":
            sys.exit()
        else:
            print("Enter a valid action\n")
    