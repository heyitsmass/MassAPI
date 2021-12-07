import os.path
import json 

class jsonParser: 

    def __init__(self, filename): 
        self.p = __file__
        self.filename = filename 
        self.output = object 
        self.searchId = ''
        self.results = dict
        self.input_terms = {
                "firstName" : '', 
                "lastName" : '', 
                "address" : '', 
                "city" : '', 
                "state" : '', 
                "zip" : '',
                "email": '', 
                "phone": '', 
        },
        self.output_terms = {}
        self.loadFile() 

    def loadFile(self): 
        
        try: 
            self.p = open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'output/' + self.filename), 'r') 
        except OSError as e: 
            print("Error: {}".format(e)) 

        self.output = json.load(self.p) 
        self.searchId = self.output['searchId'] 
        self.results = self.output['results'] 

        print("\nSearch ID ".ljust(10), ':', self.searchId.ljust(20))
        
        if len(self.results) > 0: 
            self.parseInput() 
            self.printOutput() 
        else: 
            print("No Results Found.") 
        return 

    def parseInput(self): 
        delim = 'N'

        for key in self.input_terms: 
           for value in key:  
                res_pos = [i for i, e in enumerate(value+delim) if e.isupper()]
                res_list = [value[res_pos[j]:res_pos[j+1]]
                    for j in range(len(res_pos)-1)]

                if len(res_list) > 0: 
                    self.output_terms[value.split(res_list[0])[0].capitalize() + ' ' + res_list[0]] = self.results[0][value]  
                else:
                    self.output_terms[value.capitalize()] = self.results[0][value] 
        return  

    def printOutput(self): 
        print() 
        for terms in self.output_terms: 
            print(terms.ljust(10), ':', self.output_terms[terms].ljust(20))
        print() 








