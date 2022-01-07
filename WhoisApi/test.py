filename = "information.json"
class package_array: 
    def __init__(self, index, array=[]): 
        self.index = index 
        self.array = array 

class package: 
    def __init__(self, index, array=None): 
        self.array = array 
        self.index = index 

def load_arr(data, i, arr = []):  

    while i < len(data): 
        if data[i] == '{': 
            #print("> dict begin") 
            packet = load_dict(data, i+1)
            i = packet.index+1
            arr.append(packet.array) 
            continue   
        elif data[i] == '[': 
            #print("> arr  begin") 
            i = load_arr(data, i+1).index+1 
        elif data[i] == ']':
            #print("> arr  end")
            #print(arr)  
            #return package(i, arr)
            break 
        i+=1 
    return package(i, arr) 

def load_dict(data, i, __dict_two__ = {}): 
    string = ""
    key = "" 
    saved_key = ""
    while i < len(data):
        if data[i] == '{':
            string = string.splitlines()
            for j, k in enumerate(string, 0):
                key = "" 
                value = "" 
                Key = True
                Value = False
                check = True
                if k == '' or k.isspace() or k == '\n': 
                    continue 
                string[j] = k.strip(' , ","')
                string[j] = string[j].replace('"', "") 
                for letter in string[j]: 
                    if letter == ':' and check and Key: 
                        Key = False 
                        Value = True 
                        check = False 
                    if not Value: 
                        key += letter 
                    elif not Key: 
                        value += letter 
                __dict_two__[key] = value  
            
            packet = load_dict(data, i+1)
            i = packet.index+1
            if key == '': 
                continue 
            __dict_two__[key] = packet.array
            string = "" 
            continue
        elif data[i] == '[': 
            __dict_four__ = {} 
            string = string.splitlines()
            for j, k in enumerate(string, 0): 
                key = "" 
                value = "" 
                Key = True 
                Value = False 
                check = True 
                if k == '' or k.isspace() or k == '\n' or k == ',': 
                    continue 
                string[j] = k.strip(' , "."') 
                string[j] = string[j].replace('"', "") 
                for letter in string[j]: 
                    if letter == ':' and check and Key: 
                        Key = False 
                        Value = True 
                        check = False 
                    if not Value: 
                        key += letter 
                    elif not Key: 
                        value += letter 
                
                __dict_two__[key] = value
              
            packet = load_arr(data, i)
            i = packet.index  
            __dict_two__[key] = packet.array
            continue 
        elif data[i] == '}':
            __dict__ = {} 
            string = string.splitlines()
            for j, k in enumerate(string, 0):
                key = "" 
                value = "" 
                Key = True
                Value = False
                check = True
                if k == '' or k.isspace() or k == '\n': 
                    continue 
                string[j] = k.strip(' , ","')
                string[j] = string[j].replace('"', "") 
                for letter in string[j]: 
                    if letter == ':' and check and Key: 
                        Key = False 
                        Value = True 
                        check = False 
                    if not Value: 
                        key += letter 
                    elif not Key: 
                        value += letter 
                if key == '': 
                    continue 
                __dict__[key] = value 
            return package(i, __dict__) 
        string += data[i] 
        i+=1 
    return package(i, __dict_two__) 

def load(infile, i=0): 
    __dict__ = {} 
    data = infile.read() 
    while i < len(data): 
        if data[i] == '{':
            return load_dict(data, i).array
        i+=1 
        
        

output = load(open(filename, 'r'))

print(output) 
#for key in output: 
#    print(key, output[key]) 