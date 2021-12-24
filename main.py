import curses

from plugins.ops_api.ops_menu import Menu
from plugins.ops_api.ops_auth import Authorization
from plugins.ops_api.ops_banner import Banner 


class main(object): 
    def __init__(self, scr): 
        self.screen = scr
        curses.curs_set(0) 

        main_menu_items = [('Open People Search', Menu(self.screen, func=Authorization(self.screen).menu).general_display)]
        main_menu = Menu(self.screen, Banner.sub_banners['main menu'], main_menu_items)
        main_menu.menu_display()

if __name__ == "__main__": 
    curses.wrapper(main) 
