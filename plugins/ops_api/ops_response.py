import json 
import requests 
import curses 
import os 

from .ops_parser import JsonParser
from .ops_error_codes import ErrorCode

class Response(object): 
    def __init__(self, scr):
        self.window = scr

    def getResponse(self, args, searchType, token): 
        search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/"
        search_headers = { "accept" : "text/plain", "Authorization" : "", "Content-Type" : "application/json" }
        search_headers['Authorization'] = ('Bearer {}').format(token)
        
        curses.echo() 

        for i, (key, value) in enumerate(args[1].items(), 0): 
            self.window.addstr(10+i, 46, key)
            args[0][value] = (self.window.getstr(10+i, 47+len(key), 30)).decode('UTF-8') 

            self.window.addstr(10+i, 47, '✓')
        
            response = requests.post((search_url + searchType), headers=search_headers, data=json.dumps(args[0]))
        
        curses.noecho() 

        try: 
            if response.status_code != 200: 
                raise Exception(ErrorCode.http_error(response.status_code))
        except Exception as e: 
            self.window.addstr(18, 46, '[X] Error:')
            self.window.addstr(18, 57, str(e))
            return None

        output_dir = 'output/'
        filename = output_dir + response.json()['searchId'] + '.json'

        if os.path.isdir(output_dir): 
            self.outputResponse(filename, response)
        else: 
            os.mkdir(output_dir)
            self.outputResponse(filename, response) 

        return JsonParser().loadFile(filename) 

    def outputResponse(self, filename, response): 
        try: 
            with open(filename, 'w') as output_file: 
                json.dump(response.json(), output_file)
        except FileNotFoundError as f: 
            return False 
        return True
            
