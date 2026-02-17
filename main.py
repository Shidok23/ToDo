from main_win import main_win
from list_win import list_win

state = "main_menu"

def change_win(new_win_name):
    global state

    state = new_win_name

while state is not None:
    if state == "main_menu":
        main_win(change_win)
    elif state == "list":
        list_win(change_win)
