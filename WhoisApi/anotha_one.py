filename = "information.json" 

class package: 
    def __init__(self, data, i=0): 
        self.data = data 
        self.index = i 

def load_arr(data, i=1, arr=[]): 
    while i < len(data): 
        if data[i] == ']': 
            break 
        i+=1 

    return package(arr, i+1) 
    

def load_dict(data, i=1, json={}, head='', saved_key=''): 
    final = {}
    string = key = ''

    while i < len(data): 
        if data[i] in ['{', '}', '[']:
            if type(string) == str: 
                string = string.splitlines()

            temp = {} 
            for j, k in enumerate(string, 0):
                if type(k) != list: 
                    string[j] = k.rstrip("',',': '") 
                    string[j] = string[j].lstrip()

                    string[j] = string[j].replace('"', '') 

                    key = value = '' 
                    CHECK = KEY = True 
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

                    value = value.lstrip() 

                    if key != '' and head != '':
                        temp[key] = value

                        #print(key, ':', value)
            #if len(temp) > 0: 
                #print(saved_key, ': ', temp) 

            for word in string: 
                if word in ['', '\n', ',']: 
                    string.remove(word)  
 
            string = "" 
            if data[i] == '{':
                if head == '': 
                    head = key 
                else: 
                    json[key] = {}  
                packet = load_dict(data, i+1, json, head, key)
                i = packet.index
                #print(saved_key, ': ', temp) 
                #print(key, ': ')
                print(saved_key, ': ', temp) 
                if len(temp) > 0: 
                    print(list(temp)[-1], ': ', packet.data)

                continue 
            elif data[i] == '}': 
                #print(temp)
                #print(temp) 
                if i < len(data)-1: 
                    return package(temp, i+1)
                else:
                    break 
            elif data[i] == '[':
                json[key] = []  
                packet = load_arr(data, i+1)
                i = packet.index
                print(saved_key, ': ', temp)
                
                return package(temp, i+1)  
            elif data[i] == '\n': 
                i+=1
                continue 

        string += data[i]
        i+=1

    final[head] = json 

    return package(final, i+1) 


def load(infile): 
    return load_dict(infile.read()).data

print()

output = load(open(filename, 'r')) 

print('\n', output) 
