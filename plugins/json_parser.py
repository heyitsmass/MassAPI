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
        
        self.p = open(self.filename, 'r') 

        self.output = json.load(self.p) 
        self.searchId = self.output['searchId'] 
        self.results = self.output['results'] 

        if len(self.results) > 0: 
            self.parseInput() 
        else: 
            return None 

        return self.output_terms

    def parseInput(self): 
        delim = 'N'
        # Add in functionality to parse multiple results should just need a loop and replacement of 0 in self.results[0]
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









