filename = "information.json"

class package: 
    def __init__(self, index, array=None): 
        self.array = array 
        self.index = index 
'''
def load_a(data, i, key = ""): 
    string = "" 
    while i < len(data): 
        if data[i] == '[':
            print("> arry begin:", key)
        if data[i] == '{': 
            #print("> dict begin") 
            i = load_d(data, i+1).index+1 
            continue  
        if data[i] == ']': 
            print("> arry end")
            return package(i) 

        string+=data[i]
        i += 1

    return package(i) 


def load_d(data, i): 
    string = ""
 
    __list_two__ = {} 
    while i < len(data): 
        saved_key = ""
        if data[i] == '{':
            j = len(string)-1
            key = "" 
            while j > 0: 
                if string[j] == ',' or string[j] == '{': 
                    break 
                key += string[j] 
                j-=1

            if string.find(key[::-1]): 
                string = string.replace((','+key[::-1]), "")
            
            saved_key = key[::-1].strip('\n, ,\t, , ", :') 
            print(saved_key)  
            packet = load_d(data, i+1)
            i = packet.index+1
            
            #__list_two__[saved_key] = packet.array
            continue  
        if data[i] == '[':
            j = len(string)-1
            key = "" 
            while j > 0: 
                if string[j] == ',' or string[j] == '{' or string[j] == '}': 
                    break 
                key += string[j] 
                j-=1
            key = key[::-1].strip('\n, ,\t, ", :') 
            i = load_a(data, i, key).index+1
            continue 
        if data[i] == '}': 
            string = string.splitlines()
            __list__ = {} 
            for __string__ in string:
                key = "" 
                value = "" 
                Key = True
                Value = False
                check = True  
                __string__ = __string__.strip("' ', '', ',', '\n', '\t'")

                for letter in __string__:
                    if letter == ':' and check and Key: 
                        Key = False 
                        Value = True 
                        check = False
                        continue 
                    if not Value: 
                        key += letter 
                    elif not Key: 
                        value += letter 

                if __string__ == '': 
                    continue 

                key = key.strip('", [, ]')
                value = value.strip('", ", ], [')

                print(key) 

            return package(i, __list__) 
        string += data[i] 
        i+=1 
    
    return package(i, __list_two__) 


def load(infile, i=0): 
    __dict__ = {}
    data = infile.read() 

    while i < len(data): 
        if data[i] == '{':
            packet = load_d(data, i) 
            i = packet.index+1
            #print(packet.array)
            continue 
        elif data[i] == '}': 
            print("> dict end") 
            return __dict__ 


        i+=1 

    return __dict__

'''

def load_arr(data, i): 

    while i < len(data): 
        if data[i] == '{': 
            print("> dict begin") 
            i = load_dict(data, i+1).index+1
        if data[i] == '[': 
            print("> arr  begin") 
            i = load_arr(data, i+1).index+1 
        if data[i] == ']': 
            print("> arr  end")
            return package(i) 
        i+=1 

    return package(i) 

def load_dict(data, i): 

    string = ""

    while i < len(data): 
        if data[i] == '{':
            string = string.splitlines()
            for j, k in enumerate(string, 0):
                string[j] = k.strip(' , ",", " "') 

            temp = [] 

            for word in string: 
                if word == '\n': 
                    continue 
                temp.append(word) 

            print(temp)

            print("> dict begin") 
            i = load_dict(data, i+1).index+1
            string = "" 
            continue
        elif data[i] == '[': 
            i = load_arr(data, i).index+1
            continue 
        elif data[i] == '}':
            string = string.splitlines()
            for j, k in enumerate(string, 0):  
                string[j] = k.strip(' , ","') 
            print(string) 
            print("> dict end") 
            break 

        string += data[i] 
        i+=1 

    return package(i) 

def load(infile, i=0): 
    __dict__ = {} 
    data = infile.read() 
    while i < len(data): 
        if data[i] == '{':
            i = load_dict(data, i).index
            break 

        
        i+=1 
        
        

output = load(open(filename, 'r'))



