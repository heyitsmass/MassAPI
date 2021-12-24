import curses 

class Banner: 

    sub_banners = { 
                "main menu"             : "-*-~-*-~-*-~-*-~-*- Main Menu -*-~-*-~-*-~-*-~-*-", 
                "phone search"          : "-*-~-*-~-*-~-*-~- Phone Search *-~-*-~-*-~-*-~-*-",
                "email search"          : "-*-~-*-~-*-~-*-~-* Email Search -~-*-~-*-~-*-~-*-", 
                "name search"           : "-*-~-*-~-*-~-*-~-* Name Search *-~-*-~-*-~-*-~-*-", 
                "name address search"   : "-*-~-*-~-*-~-* Name/Address Search *-~-*-~-*-~-*-", 
                "name dob search"       : "-*-~-*-~-*-~-*-~ Name/DOB Search ~-*-~-*-~-*-~-*-", 
                "business search"       : "-*-~-*-~-*-~-*-~ Business Search ~-*-~-*-~-*-~-*-", 
                "address search"        : "-*-~-*-~-*-~-*-~- Address Search ~-*-~-*-~-*-~-*-", 
                "pobox search"          : "-*-~-*-~-*-~-*-~ P.O. BOX Search ~-*-~-*-~-*-~-*-",
                'ops login'             : "-*-~-*-~-*-~ Open People Search Login -*-~-*-~-*-",
                "OPS API"               : "-*-~-*-~-*-~- Open People Search API ~-*-~-*-~-*-",
                "OPS Results"           : "-*-~-*-~-*-~-*-~-*-* Results *-*-~-*-~-*-~-*-~-*-" 
    }

    def __init__(self):
        pass 

    def display_banner(self): 
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK) 
        
        self.window.addstr(0, 50, "___  ___                 ___  ______ _____", curses.color_pair(1))
        self.window.addstr(1, 50, "|  \/  |                / _ \ | ___ \_   _|", curses.color_pair(1))
        self.window.addstr(2, 50, "| .  . | __ _ ___ ___  / /_\ \| |_/ / | |", curses.color_pair(1))
        self.window.addstr(3, 50, "| |\/| |/ _` / __/ __| |  _  ||  __/  | |", curses.color_pair(1))
        self.window.addstr(4, 50, "| |  | | (_| \__ \__ \ | | | || |    _| |_", curses.color_pair(1))
        self.window.addstr(5, 50, "\_|  |_/\__,_|___/___/ \_| |_/\_|    \___/", curses.color_pair(1))
        self.window.addstr(6, 53, "-~*- An API ", curses.color_pair(1))
        self.window.addstr(6, 65, "practice", curses.color_pair(2))
        self.window.addstr(6, 74, "environment -*~", curses.color_pair(1))
