import json

import curses 
from curses import panel

import requests

import os 
import tempfile
import time 

class Banner: 
    def __init__(self):
        pass 
    
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
                "OPS API"               : "-*-~-*-~-*-~- Open People Search API ~-*-~-*-~-*-",
                "OPS Results"           : "-*-~-*-~-*-~-*-~-*-* Results *-*-~-*-~-*-~-*-~-*-" 
        }

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

class JsonParser: 
    def __init__(self, scr):
        self.window = scr.subwin(0, 0) 
        self.window.keypad(1) 
        self.panel = panel.new_panel(self.window) 
        self.panel.hide() 
        panel.update_panels() 
        pass

    def loadFile(self, filename = None):    #Add error checking for filename

        if filename != None: 
            in_file = open(filename, 'r') 
            output = json.load(in_file)  
            results = output['results']

            if len(results) > 0: 
                output = self.parseInput(results) 
                return output
            
        return None
    
    def parseInput(self, results): 
        delim = ''
        output = []

        for index in range(len(results)): 
            sub_list = []
            for key in results[index]: 
                value = str(results[index][key])

                if not value.find('http') or not value.find('https') or len(value) > 30:
                    results[index][key] = 'Check output file'
                elif value == '':
                    continue

                for letter in key: 
                    if letter.isupper(): 
                        delim = letter 
                
                new_key = key.split(delim) 

                if len(new_key) > 1: 
                    new_key = new_key[0].capitalize() + ' ' + delim + new_key[1] + ': ' + str(results[index][key])
                else: 
                    new_key = new_key[0].capitalize() + ': ' + str(results[index][key])
                
                sub_list.append(new_key)  
            output.append(sub_list)

        return output

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

            self.json_display(func = self.func, output=self.func())

            break
        
        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate()
        return 

    def json_display(self, func, output = [], curr = 0): 
        self.panel.top() 
        self.panel.show() 
        self.window.clear() 

        while True: 
            self.window.refresh() 
            curses.doupdate() 
            Banner.display_banner(self)

            line = 0
            self.window.addstr(7, 46, Banner.sub_banners['OPS Results'])
            if len(output) > 0: 
                for j, word in enumerate(output[curr], 0):
                    self.window.addstr(9 + j, 48, word)
                    line = 10 + (j+1) 
            else: 
                self.window.addstr(0, 15, 'No output returned from search.') 

            self.window.addstr(line, 48, 'Perform another search? (Y/N)')
            self.window.addstr(line+2, 48, 'Navigate results using ← or →')

            key = self.window.getch()
            if key in [curses.KEY_ENTER, ord('\n')]:
                break
            elif key in [curses.KEY_RIGHT]:
                if curr+1 < len(output):  
                    self.json_display(func, output=output, curr=curr+1) 
                    return
            elif key in [curses.KEY_LEFT]:
                if curr-1 >= 0:  
                    self.json_display(func, output=output, curr=curr-1)
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

class Search(object): 
    def __init__(self, scr, token):
        self.authToken = token 
        self.window = scr
    
    def phone(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['phone search']) 
        searchType = 'PhoneSearch'
        args = [{
            'phoneNumber' : ''
        }, {
            '[X] Enter phone number:' : 'phoneNumber' 
        }]

        return Response(self.window, args, searchType, self.authToken).getResponse() 

    
    def email(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['email search'])
        searchType = 'EmailAddressSearch'
        args = [{
            'emailAdress' : ''
        }, {
            '[X] Enter email address:' : 'emailAddress'
        }]        

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def name(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name search']) 
        searchType = 'NameSearch'
        args = [{
            'firstName' : '', 
            'middleName' : '', 
            'lastName' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter first name (required):' : 'firstName' ,
            '[X] Enter middle name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter city (optional):' : 'city',
            '[X] Enter state (optional):' : 'state'   

        }]

        'firstName'     #Partial okay
        'middleName'    #Opt 
        'lastName' 
        'city'          #Opt
        'state'         #Opt

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def nameAddress(self): 
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name address search']) 
        searchType = 'NameAddressSearch'
        args = [{ 
            'firstName' : '',#Opt
            'lastName' : '',
            'address' : '', 
            'unit'   : '',   #Opt
            'city' : '',
            'state' : ''
        }, { 
            '[X] Enter first name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter address (required):' : 'address',
            '[X] Enter unit # (optional):' : 'unit',   
            '[X] Enter city (required):' : 'city',
            '[X] Enter state (required):' : 'state'       
        }]

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def nameDOB(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name dob search']) 
        searchType = 'nameDOBSearch'
        args = [{
            'firstName' : '', 
            'lastName' : '', 
            'dob' : ''
        }, {
            '[X] Enter first name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter DOB (required):' : 'dob'
        }]

        'firstName' #partial okay
        'lastName' 
        'dob'       # DD/MM/YYY or 00/00/YYY

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def business(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['business search']) 
        searchType = 'BusinessSearch'
        args = [{
            'businessName' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter Business Name (required):' : 'businessName', 
            '[X] Enter city (optional):' : 'city', 
            '[X] Enter state (optional):' : 'state'          
        }]

        'businessName' 
        'city' #Opt
        'state' #Opt    
        #City/State or State

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def address(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['address search']) 
        searchType = 'AddressSearch'
        args = [{
            'address' : '', 
            'unit' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter Address (required):' : 'address', 
            '[X] Enter unit (optional):' : 'unit', 
            '[X] Enter city (required):' : 'city', 
            '[X] Enter state (required):' : 'state'
        }]

        return Response(self.window, args, searchType, self.authToken).getResponse()

    def poBox(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['pobox search'])
        searchType = 'PoBoxSearch'
        args = [{
            'poBox' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter PO Box (required):' : 'poBox', 
            '[X] Enter City (required):' : 'city', 
            '[X] Enter State (required):' : 'state'
        }]

        return Response(self.window, args, searchType, self.authToken).getResponse()

class UserInfo(object): 

    def __init__(self, username = '', password = ''): 
        self.username = username
        self.password = password 

class Response(object): 
    def __init__(self, scr, args=None, searchType=None, token=None):
        self.search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/"
        self.search_headers = { "accept" : "text/plain", "Authorization" : "", "Content-Type" : "application/json" }
        self.search_headers['Authorization'] = ('Bearer {}').format(token)
        self.window = scr

        self.args = args 
        self.searchType = searchType 

    def http_error(self, e): 
        codes = { 
            400 : 'Bad Request', 
            401 : 'Unauthorized', 
            402 : 'Payment Required', 
            413 : 'Development Bug', 
            500 : 'Internal Server Error', 
            503 : 'Temporarily Unavailable', 
            200 : 'Valid request' 
        }
        return codes.get(e, 'Null error') 

    def getResponse(self): 
        curses.echo() 

        for i, (key, value) in enumerate(self.args[1].items(), 0): 
            self.window.addstr(10+i, 46, key)
            self.args[0][value] = (self.window.getstr(10+i, 47+len(key), 30)).decode('UTF-8') 

            self.window.addstr(10+i, 47, '✓')

            #filename = 'output/2de2e9122289434eb53379a07422fede.json'
            #return JsonParser(self.window).loadFile(filename) 
        
            response = requests.post((self.search_url + self.searchType), headers=self.search_headers, data=json.dumps(self.args[0]))

        try: 
            if response.status_code != 200: 
                raise Exception(self.http_error(response.status_code))
        except Exception as e: 
            self.window.addstr(18, 46, '[X] Error:')
            self.window.addstr(18, 57, str(e))
            return None

        filename = ('output/' + response.json()['searchId'] + '.json')

        with open(filename, 'w') as output_file: 
            json.dump(response.json(), output_file)
        
        return JsonParser(self.window).loadFile(filename) 

class Authorization(object): 
    def __init__(self, scr):
        self.screen = scr 
        self.TOKEN_PATH = os.path.join(
            tempfile.gettempdir(),
            'libname', 
            'ops.token'
        )

        self.MAX_AGE = 5040 * 60 


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

    def menu(self): 
        token = None 

        if os.path.isfile(self.TOKEN_PATH): 
            token_age = time.time() - os.path.getmtime(self.TOKEN_PATH) 
            if token_age < self.MAX_AGE: 
                with open(self.TOKEN_PATH, 'r') as in_file: 
                    token = in_file.read() 
        if not token: 
            userinfo = self.getPayload() 
            token = self.getAuth(userinfo) 

            with open(self.TOKEN_PATH, 'w') as out_file: 
                out_file.write(token) 

        if token: 
            items = [ 
                    ('Phone Search', Menu(self.screen, func=Search(self.screen, token).phone).response_display), 
                    ('Email Address Search', Menu(self.screen, func=Search(self.screen, token).email).response_display), 
                    ('Name Search', Menu(self.screen, func=Search(self.screen, token).name).response_display), 
                    ('Name & Address Search', Menu(self.screen, func=Search(self.screen, token).nameAddress).response_display), 
                    ('Name & DOB Search', Menu(self.screen, func=Search(self.screen, token).nameDOB).response_display), 
                    ('Business Search', Menu(self.screen, func=Search(self.screen, token).business).response_display), 
                    ('Address Search', Menu(self.screen, func=Search(self.screen, token).address).response_display), 
                    ('PO Box Search', Menu(self.screen, func=Search(self.screen, token).poBox).response_display)    
            ]

            searchMenu = Menu(self.screen, Banner.sub_banners['OPS API'], items)
            searchMenu.menu_display() 
            
        return 

class main(object): 
    def __init__(self, scr): 
        self.screen = scr
        curses.curs_set(0) 

        main_menu_items = [('Open People Search', Menu(self.screen, func=Authorization(self.screen).menu).general_display)]
        main_menu = Menu(self.screen, Banner.sub_banners['main menu'], main_menu_items)
        main_menu.menu_display()

if __name__ == "__main__": 
    curses.wrapper(main) 
