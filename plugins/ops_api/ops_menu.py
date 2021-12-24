import curses 
from curses import panel

from .ops_banner import Banner 

class Menu(object): 
    def __init__(self, stdscreen, banner = '', items = [], func = None): 
        self.window = stdscreen.subwin(0, 0) 
        self.window.keypad(1) 
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.banner = banner 

        self.position = 0
        self.items = items 

        self.func = func

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
    
    def menu_display(self): 
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True: 
            self.window.refresh()
            curses.doupdate()
            Banner.display_banner(self) 
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
    
    def general_display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True: 
            self.window.refresh() 
            curses.doupdate()
            Banner.display_banner(self) 
            self.window.addstr(8, 46, self.banner) 

            self.func()

            break 
        
        self.window.clear() 
        self.panel.hide() 
        panel.update_panels()
        curses.doupdate()

        return


    def response_display(self): 
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh() 
            curses.doupdate()  

            self.json_display(func = self.func, output=self.func()) #output changed to a package of information

            break
        
        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate()
        return 

    def json_display(self, func, output, curr = 0):    #output decoded as a package of information
        self.panel.top() 
        self.panel.show() 
        self.window.clear() 

        while True: 
            self.window.refresh() 
            curses.doupdate() 
            Banner.display_banner(self)

            line = 0
            self.window.addstr(7, 46, Banner.sub_banners['OPS Results'])
            if len(output.output) > 0: 
                for j, word in enumerate(output.output[curr], 0):
                    self.window.addstr(9 + j, 48, word)
                    line = 10 + (j+1) 
                self.window.addstr(line, 48, "Results outputted to: ")
                self.window.addstr((line+1), 48, ('/' + output.filename))
                line += 3
            else: 
                self.window.addstr(0, 15, 'No output returned from search.') 

            self.window.addstr(line, 48, 'Perform another search? (Y/N)')
            self.window.addstr(line+2, 48, 'Navigate results using ← or →')

            key = self.window.getch()
            if key in [curses.KEY_ENTER, ord('\n')]:
                break
            elif key in [curses.KEY_RIGHT]:
                if curr+1 < len(output.output):  
                    self.json_display(func, output, curr=curr+1) 
                    return
            elif key in [curses.KEY_LEFT]:
                if curr-1 >= 0:  
                    self.json_display(func, output, curr=curr-1)
                    return
            elif key == ord(('N').lower()): 
                return  
            elif key == ord(('Y').lower()): 
                Menu(self.window, func=func).response_display()
                return 
            else: 
                pass 
     
        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate() 
        
        return      
