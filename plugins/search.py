import curses 
from curses import panel

from .resources.banners import banners 
from .resources.banners import sub_banners
from .json_parser import jsonParser as jp

import requests 
import json 

class response(object): 
    def __init__(self, args, searchType, token, stdscreen): 

        self.search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/"
        self.search_headers = { "accept" : "text/plain", "Authorization" : "", "Content-Type" : "application/json" }
        self.search_headers['Authorization'] = ('Bearer {}').format(token)
        self.window = stdscreen

        self.args = args 
        self.searchType = searchType 
        pass 

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
        
        search_response = requests.post((self.search_url + self.searchType), headers=self.search_headers, data=json.dumps(self.args[0]))

        try: 
            if search_response.status_code != 200: 
                raise Exception(self.http_error(search_response.status_code))
        except Exception as e: 
            self.window.addstr(18, 46, '[X] Error:')
            self.window.addstr(18, 57, str(e))
            return None
        
        return search_response
    

        

class display(object): 

    def __init__(self, stdscreen, func): 
        self.window = stdscreen.subwin(0, 0) 
        self.window.keypad(1) 
        self.panel = panel.new_panel(self.window) 
        self.panel.hide() 
        self.func = func 
        self.screen = stdscreen
        panel.update_panels()

    def display(self): 
        self.panel.top()
        self.panel.show() 
        self.window.clear() 

        while True:
            self.window.refresh() 
            curses.doupdate() 

            response = self.func()

            self.displayResponse(response)

            self.window.addstr(22, 47, 'Perform another search? (Y/N)')

            key = self.window.getch() 
            if key == ord(('N').lower()): 
                break 
            elif key == ord(('Y').lower()): 
                display(self.screen, self.func).display()
                return 
            else: 
                pass 
        
        self.window.clear() 
        self.panel.hide() 
        panel.update_panels() 
        curses.doupdate() 
    
    def displayResponse(self, response = None): 
        if response: 
                filename = ('output/' + response.json()['searchId'] + '.json')

                with open(filename, 'w') as output_file: 
                    json.dump(response.json(), output_file)
                try: 
                    output = jp(filename).loadFile() 
                    
                    if filename == None: 
                        raise(Exception('[X] Error processing request.'))
                except Exception as e: 
                    self.window.addstr(16, 46, str(e))
                    return 
    
                if output == None: 
                    self.window.addstr(16, 46, '[X] No immediate results found.')
                else: 
                    self.window.clear() 
                    banners.display_banner(self) 
                    self.window.addstr(8, 46, sub_banners['OPS Results']) 
                    for i, (key, item) in enumerate(output.items(), 0):
                        new_key = '%s:' % key
                        self.window.addstr(10 + i, 47, new_key) 
                        self.window.addstr(10 + i, 48 + len(new_key), item) 
                self.window.addstr(19, 47, 'Search results outputted to:')
                self.window.addstr(20, 47, ('/' + filename))      
            
                return 
        return 
    

class search(object):
    
    def __init__(self, stdscreen, token): 
        self.authToken = token
        self.window = stdscreen

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
    
    
    def phone(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['phone search']) 
        searchType = 'PhoneSearch'
        args = [{
            'phoneNumber' : ''
        }, {
            '[X] Enter phone number:' : 'phoneNumber' 
        }]

        'phoneNumber'

        return response(args, searchType, self.authToken, self.window).getResponse() 

    
    def email(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['email search'])
        searchType = 'EmailAddressSearch'
        args = [{
            'emailAdress' : ''
        }, {
            '[X] Enter email address:' : 'emailAddress'
        }]        

        'emailAddress'
        
        return response(args, searchType, self.authToken, self.window).getResponse()

    def name(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['name search']) 
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

        return response(args, searchType, self.authToken, self.window).getResponse()

    def nameAddress(self): 
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['name address search']) 
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

        return response(args, searchType, self.authToken, self.window).getResponse()

    def nameDOB(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['name dob search']) 
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

        return response(args, searchType, self.authToken, self.window).getResponse()

    def business(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['business search']) 
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

        return response(args, searchType, self.authToken, self.window).getResponse()

    def address(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['address search']) 
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

        return response(args, searchType, self.authToken, self.window).getResponse()

    def poBox(self):
        banners.display_banner(self)  
        self.window.addstr(8, 46, sub_banners['pobox search'])
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

        return response(args, searchType, self.authToken, self.window).getResponse()
