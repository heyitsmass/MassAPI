import os
from .colors import Colors as color

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
