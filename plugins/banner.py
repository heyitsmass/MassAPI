class banner: 
    def __init__(self): 
        self.width = 100
    
    def display(self): 
        print("___  ___                 ___  ______ _____".center(self.width))
        print(" |  \/  |                / _ \ | ___ \_   _|".center(self.width))
        print("| .  . | __ _ ___ ___  / /_\ \| |_/ / | |".center(self.width))
        print("| |\/| |/ _` / __/ __| |  _  ||  __/  | |".center(self.width))
        print("| |  | | (_| \__ \__ \ | | | || |    _| |_".center(self.width)) 
        print("\_|  |_/\__,_|___/___/ \_| |_/\_|    \___/".center(self.width))
        print("-~*- An API practice environment -*~-".center(self.width))
