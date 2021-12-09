import os
import cursor 
import curses
from curses import wrapper
from .colors import Colors as color
from .banner import banner 

class Menu: 

    def __init__(self, **auth_data): 
        self = auth_data

    def display(self): 

        self["username"] = input(f"{color.WHT}[{color.RED}-{color.WHT}] Username: {color.RST}")
        os.system('clear')
        print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Username: {color.RST}" + ('*' * int(len(self["username"]) / 2)))

        self["password"] = input(f"{color.WHT}[{color.RED}-{color.WHT}] Password: {color.RST}") 
        os.system('clear')
        print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Username: {color.RST}" + ('*' * int(len(self["username"]) / 2)))
        print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Password: {color.RST}" + ('*' * int(len(self["password"]) / 2)))

        return 

    def key_listener(win): 
        win.nodelay(True)
        key = ''
        win.clear()
        win.addstr("Detected key: ") 
        while True: 
            try: 
                key = win.getkey() 
                win.clear() 
                win.addstr("Detected key: ") 
                win.addstr(str(key)) 
                if key == os.linesep: 
                    break 
            except Exception as e: 
                pass 

    def main_menu():

        cursor.hide() 

        banner().display() 

        #print()
        #print("-*-~-*-~-*-~-*-~-*- Main Menu -*-~-*-~-*-~-*-~-*-".center(100))
        #print("1. Phone number search".rjust(50))

        #stdscr = curses.initscr()


                                           
        return 

    #curses.wrapper(key_listener)