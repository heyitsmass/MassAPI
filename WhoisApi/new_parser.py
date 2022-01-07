FILENAME = "geolocation.json"


class package: 
    def __init__(self, array, index): 
        self.array = array 
        self.index = index


def load_arr(data, i=0, arr=[], json={}): 
    
    while i < len(data): 
        if data[i] in ['{', '[', ']']: 
            if data[i] == '{': 
                print("> dict begin")
                i = load_dict(data, i+1, json).index+1
                continue 
            elif data[i] == '[': 
                print("> arr begin")
                i = load_arr(data, i+1, json).index+1
                continue 
            elif data[i] == ']': 
                print("< arr end") 
                break 
        i+=1

    return package(arr, i)  

def load_dict(data, i=0 , json={}): 
    string = "" 
    while i < len(data): 
        if data[i] in ['{', '}', '[']: 
            string = string.splitlines() 
            for j, k in enumerate(string, 0): 
                key = "" 
                value = "" 
                KEY = True
                VALUE = False
                CHECK = True
                string[j] = k.strip()

                if k == ',': 
                    continue 
                
                string[j] = k.strip(" , ','")
                string[j] = string[j].replace('"', "") 

                for letter in string[j]: 
                    if letter == ':' and CHECK and KEY: 
                        KEY = False 
                        VALUE = True 
                        CHECK = False
                        continue 
                    if not VALUE: 
                        key += letter 
                    if not KEY: 
                        value += letter
                if key != '':   
                    print(value) 
            for word in string: 
                if word == '' or word == ',': 
                    string.remove(word) 

            string = "" 
            if data[i] == '{':
                print("> dict begin")
                i = load_dict(data, i+1, json).index+1
                continue 
            elif data[i] == '}': 
                print("< dict end") 
                break
            elif data[i] == '[': 
                print("> arr begin") 
                i = load_arr(data, i+1, json).index+1
                continue 

        string += data[i] 
        i+=1 

    return package(json, i) 

def load(infile): 
    data = infile.read()
    return load_dict(data).array 


print(load(open(FILENAME, 'r')))