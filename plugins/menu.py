import curses
from   curses import panel

from .resources.banners import banners 

class Menu(object): 
    def __init__(self, items, stdscreen, banner): 
        self.window = stdscreen.subwin(0, 0) 
        self.window.keypad(1) 
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.banner = banner 

        self.position = 0
        self.items = items 

        if self.banner.find('Main Menu') != -1: 
            self.items.append(('Exit', 'Exit'))
        else: 
            self.items.append(('Back', 'Back'))

    def navigate(self, n): 
        self.position += n
        if self.position < 0: 
            self.position = 0
        elif self.position >= len(self.items): 
            self.position = len(self.items) - 1
    
    def display(self): 
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True: 
            self.window.refresh()
            curses.doupdate()
            banners.display_banner(self) 
            self.window.addstr(8, 46, self.banner) 
            for index, item in enumerate(self.items): 
                if index == self.position: 
                    mode = curses.A_REVERSE
                else: 
                    mode = curses.A_NORMAL
                
                msg = "%d. %s" % (index +1, item[0])
                self.window.addstr(9+index, 48, msg, mode) 
            
            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]: 
                if self.position == len(self.items) - 1: 
                    break 
                else: 
                    self.items[self.position][1]()
            elif key == curses.KEY_UP: 
                self.navigate(-1) 

            elif key == curses.KEY_DOWN: 
                self.navigate(1)

        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate()