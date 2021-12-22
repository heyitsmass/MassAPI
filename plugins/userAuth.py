import curses
from curses import panel

from .resources.banners import sub_banners
from .resources.banners import banners
from .search import display
from .search import search 
from .menu import Menu 

import requests 

import json

import os 
import time 
import tempfile 

TOKEN_PATH = os.path.join(
    tempfile.gettempdir(),
    'libname', 
    'ops.token'
)

MAX_AGE = 5040 * 60

class OPS_Auth(object): 

    def __init__(self, stdscreen, banner = sub_banners['OPS API']): 
        self.screen = stdscreen
        self.window = stdscreen.subwin(0, 0) 
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window) 
        self.panel.hide() 
        panel.update_panels()

        self.banner = banner 

    def getPayload(self):
        self.window.addstr(9, 46, '[X] Username:') 
        curses.echo() 
        u = (self.window.getstr(9, 60, 43)).decode('UTF-8')
        self.window.addstr(9, 47, '✓')

        self.window.addstr(10, 46, '[X] Password:') 
        p = (self.window.getstr(10, 60, 43)).decode('UTF-8') 
        curses.noecho()
        self.window.addstr(10, 47, '✓')
        self.window.addstr(10, 60, ('*' * int(len(p)))) 

        return userinfo(u, p) 

    def http_error(self, e): 
        codes = { 
            400 : 'Invalid username and/or password', 
            401 : 'Unauthorized', 
            402 : 'Payment Required', 
            413 : 'Development Bug', 
            500 : 'Internal Server Error', 
            503 : 'Temporarily Unavailable', 
            200 : 'Valid request' 
        }

        return codes.get(e, 'Null error')        

    def getAuth(self, userinfo):


            
        auth_url = "https://api.openpeoplesearch.com/api/v1/User/authenticate"
        auth_data = { "username" : "", "password" : ""}
        auth_headers = { "Content-Type" : "application/json", "accept" : "*/*" } 
         
        auth_data['username'] = userinfo.username 
        auth_data['password'] = userinfo.password 

        try: 
            auth_response = requests.post(auth_url, headers=auth_headers, data=json.dumps(auth_data))

            if auth_response.status_code != 200: 
                raise Exception(self.http_error(auth_response.status_code))

            token = auth_response.json()['token']
        
        except Exception as e: 
            self.window.addstr(12, 46, '[X] User Authentication Error:') 
            self.window.addstr(12, 77, str(e))
            return None

        return token         

    def display(self): 
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True: 
            self.window.refresh() 
            curses.doupdate() 
            banners.display_banner(self) 
            self.window.addstr(8, 46, self.banner) 

            token = None 

            if os.path.isfile(TOKEN_PATH): 
                token_age = time.time() - os.path.getmtime(TOKEN_PATH) 

                if token_age < MAX_AGE: 
                    with open(TOKEN_PATH, 'r') as infile: 
                        token = infile.read()
            if not token:

                userinfo = self.getPayload() 
    
                token = self.getAuth(userinfo) 

                with open(TOKEN_PATH, 'w') as outfile: 
                    outfile.write(token) 

            if token: 
                self.window.addstr(12, 46, 'User Authenticated.') 
                items = [
                    ('Phone Search', display(self.screen, search(self.screen, token).phone).display), 
                    ('Email Address Search', display(self.screen, search(self.screen, token).email).display), 
                    ('Name Search', display(self.screen, search(self.screen, token).name).display), 
                    ('Name & Address Search', display(self.screen, search(self.screen, token).nameAddress).display), 
                    ('Name & DOB Search', display(self.screen, search(self.screen, token).nameDOB).display), 
                    ('Business Search', display(self.screen, search(self.screen, token).business).display), 
                    ('Address Search', display(self.screen, search(self.screen, token).address).display), 
                    ('PO Box Search', display(self.screen, search(self.screen, token).poBox).display)
                ]

                searchMenu = Menu(items, self.screen, self.banner)
                searchMenu.display()

                break 

            key = self.window.getch() 

            if key in [curses.KEY_ENTER, ord('\n')]: 
                break 

        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate() 

        return 

class userinfo(object): 

    def __init__(self, username = '', password = ''): 
        self.username = username
        self.password = password 

