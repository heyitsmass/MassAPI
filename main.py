from plugins.menu import Menu 
import curses
from curses import panel

from plugins.userAuth import OPS_Auth
from plugins.resources.banners import sub_banners

class main(object): 
    def __init__(self, stdscreen): 
        self.screen = stdscreen 
        curses.curs_set(0)

        main_menu_items = [('Open People Search', OPS_Auth(self.screen).display)]
        main_menu = Menu(main_menu_items, self.screen, sub_banners['main menu'])

        main_menu.display()

if __name__ == "__main__": 
    curses.wrapper(main)