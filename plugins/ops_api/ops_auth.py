import os 
import tempfile 
import time
import curses
import requests
import json  

from .ops_menu import Menu 
from .ops_search import Search 
from .ops_banner import Banner 
from .ops_error_codes import ErrorCode

class UserInfo(object): 

    def __init__(self, username = '', password = ''): 
        self.username = username
        self.password = password 

class Authorization(object): 
    def __init__(self, scr):
        self.window = scr 
        '''        
        self.TOKEN_PATH = os.path.join(
            tempfile.gettempdir(),
            'libname', 
            'ops.token'
        )
        '''
        self.MAX_AGE = 5040 * 60 
    
    def getPayload(self):
        Banner.display_banner(self) 
        self.window.addstr(8, 46, Banner.sub_banners['ops login'])
        self.window.addstr(9, 46, '[X] Username:') 
        curses.echo() 
        u = (self.window.getstr(9, 60, 43)).decode('UTF-8')
        self.window.addstr(9, 47, '✓')

        self.window.addstr(10, 46, '[X] Password:') 
        p = (self.window.getstr(10, 60, 43)).decode('UTF-8') 
        curses.noecho()
        self.window.addstr(10, 47, '✓')
        self.window.addstr(10, 60, ('*' * int(len(p)))) 

        return UserInfo(u, p)

    def getAuth(self, userinfo):

        auth_url = "https://api.openpeoplesearch.com/api/v1/User/authenticate"
        auth_data = { "username" : "", "password" : ""}
        auth_headers = { "Content-Type" : "application/json", "accept" : "*/*" } 
         
        auth_data['username'] = userinfo.username 
        auth_data['password'] = userinfo.password 

        try: 
            auth_response = requests.post(auth_url, headers=auth_headers, data=json.dumps(auth_data))

            if auth_response.status_code != 200: 
                raise Exception(ErrorCode.http_error(auth_response.status_code))

            token = auth_response.json()['token']
        
        except Exception as e: 
            self.window.addstr(12, 46, '[X] User Authentication Error:') 
            self.window.addstr(12, 77, str(e))
            return None

        return token

    def menu(self): 
        token = None 


        TOKEN_PATH = os.path.join(tempfile.gettempdir(), 'ops api') 
        if os.path.isdir(TOKEN_PATH): 
            TOKEN_PATH = os.path.join(TOKEN_PATH, 'ops.token')
        else: 
            os.mkdir(TOKEN_PATH)
            TOKEN_PATH = os.path.join(TOKEN_PATH, 'ops.token') 

        if os.path.isfile(TOKEN_PATH): 
            token_age = time.time() - os.path.getmtime(TOKEN_PATH) 
            if token_age < self.MAX_AGE: 
                with open(TOKEN_PATH, 'r') as in_file: 
                    token = in_file.read() 
        if not token: 
            userinfo = self.getPayload() 
            token = self.getAuth(userinfo) 

            with open(TOKEN_PATH, 'w') as out_file: 
                out_file.write(token) 

        if token: 
            items = [ 
                    ('Phone Search', Menu(self.window, func=Search(self.window, token).phone).response_display), 
                    ('Email Address Search', Menu(self.window, func=Search(self.window, token).email).response_display), 
                    ('Name Search', Menu(self.window, func=Search(self.window, token).name).response_display), 
                    ('Name & Address Search', Menu(self.window, func=Search(self.window, token).nameAddress).response_display), 
                    ('Name & DOB Search', Menu(self.window, func=Search(self.window, token).nameDOB).response_display), 
                    ('Business Search', Menu(self.window, func=Search(self.window, token).business).response_display), 
                    ('Address Search', Menu(self.window, func=Search(self.window, token).address).response_display), 
                    ('PO Box Search', Menu(self.window, func=Search(self.window, token).poBox).response_display)    
            ]

            searchMenu = Menu(self.window, Banner.sub_banners['OPS API'], items)
            searchMenu.menu_display() 
            
        return 
