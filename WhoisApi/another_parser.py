filename = "information.json" 


class package: 
    def __init__(self, data, i): 
        self.data = data 
        self.index = i 

def load_arr(data, i=0, json={}, arr=[]): 
    while i < len(data): 
        if data[i] == ']': 
            return package(arr, i+1) 
        i+=1 

    return package(arr, i+1) 

def load_dict(data, i=0, json={}):
    string = ""
    while i < len(data):  
        #print(data[i], end='')
        if data[i] in ['{', '}', '[', ']']:
            string = string.lstrip(',')
            string = string.splitlines()
            for j, k in enumerate(string, 0): 
                string[j] = k.lstrip()
                string[j] = string[j].rstrip("',',': '")
            
            for word in string:
                if word == '' or word == '\n': 
                    string.remove(word) 

            if len(string) >= 1 and string[0] != '':
                #print(string, '\n') 
                pass

            if data[i] == '{':
                #print("> dict begin")
                __temp__ = {} 
                saved_key = "" 
                if len(string) >= 1 and string[0] != '':
                    saved_key = string[len(string)-1]
                    #print(k)
                    #string = string.remove(k)
                    if len(string) > 1: 
                        string.remove(saved_key)

                        for j, k in enumerate(string, 0): 
                            key = value = ''
                            KEY = CHECK = True 
                            VALUE = False 
                            for letter in string[j]: 
                                if letter == ':' and CHECK and KEY: 
                                    KEY = CHECK = False 
                                    VALUE = True 
                                    continue 
                                if not VALUE: 
                                    key += letter 
                                if not KEY: 
                                    value += letter
                            __temp__[key] = value 
                        #print(__temp__)
                    __temp__[saved_key] = '' 
                    #print(__temp__)

                packet = load_dict(data, i+1, __temp__)
                i = packet.index
                if i < len(data)-1: 
                    print(packet.data)
                
                string = ""
                pass
            elif data[i] == '}':
                __temp2__ = {}
                #print(len(list(json)))
                #print(list(json)[-1]) 
                if len(string) >= 1 and string[0] != '': 
                    for j, k in enumerate(string, 0): 
                        key = value = '' 
                        KEY = CHECK = True 
                        VALUE = False 
                        for letter in string[j]: 
                            if letter == ':' and CHECK and KEY: 
                                KEY = CHECK = False
                                VALUE = True 
                                continue 
                            if not VALUE: 
                                key += letter 
                            if not KEY: 
                                value += letter 
                        __temp2__[key] = value
                         
                    if len(json) >= 1: 
                        json[list(json)[-1]] = __temp2__ 
                    else: 
                        string = "" 
                        return package(__temp2__, i+1) 
                    
                string = ""
                return package(json, i+1) 
            elif data[i] == '[':
                i = load_arr(data, i+1, json).index
                string = "" 
                continue 
            elif data[i] == ']': 
                #print("> arr end") 
                string = ""
                i+=1
                pass 
        if i > len(data): 
            return package(json, i) 

        string += data[i]
        i+=1 

    return package(json, i+1) 

def load(infile): 
    return load_dict(infile.read())

print('\n', load(open(filename, 'r')).data)

