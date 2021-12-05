import json 
import os.path

class jsonParser: 

    def __init__(self): 
        self.p = __file__
        self.output = object
        self.searchId = int
        self.results = list
        self.input_terms = {
                "firstName" : '', 
                "lastName" : '', 
                "address" : '', 
                "city" : '', 
                "state" : '', 
                "zip" : ''
        }
        self.output_terms = {}

    def checkResults(self): 
        if len(self.results) > 0: 
            return True 
        else:
            return False 
    
    def loadFile(self): 
        try: 

            self.p = open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'output/output.json'), 'r') 
        
        except OSError as e: 

            print("Error: {}".format(e)) 

        self.output = json.load(self.p) 

        self.searchId = self.output['searchId'] 
        self.results = self.output['results'] 

        print("\nSearch ID".ljust(10), ':', self.searchId.ljust(20))
        
        if self.checkResults(): 
            print("Results Found.") 
        else: 
            print("No Results Found.") 
        
        return 

    def parseInput(self): 
        delim = 'N'

        for key in self.input_terms: 
            
            res_pos = [i for i, e in enumerate(key+delim) if e.isupper()]
            res_list = [key[res_pos[j]:res_pos[j+1]]
                for j in range(len(res_pos)-1)]

            if len(res_list) > 0: 
                self.output_terms[key.split(res_list[0])[0].capitalize() + ' ' + res_list[0]] = self.input_terms[key]
            else:
                self.output_terms[key.capitalize()] = self.input_terms[key]

        return 

    def printOutput(self): 
        for terms in self.output_terms: 
            print(terms.ljust(10), ':', self.output_terms[terms].ljust(20))
        print() 






