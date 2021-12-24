import json

class Output: 
    def __init__(self, output, filename): 
        self.output = output
        self.filename = filename

class JsonParser: 
    def __init__(self):
        pass

    def loadFile(self, filename = None):    #Add error checking for filename

        if filename != None: 
            in_file = open(filename, 'r') 
            output = json.load(in_file)  
            results = output['results']

            if len(results) > 0: 
                return Output(self.parseInput(results), filename) 
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
