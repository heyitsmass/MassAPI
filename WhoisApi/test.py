filename = "geolocation.json" 

final = {} 

key = ''
value = ''

temp = {} 
'''
with open(filename, 'r') as outfile: 
    data =  outfile.read()
    for i in range(len(data)):
        if data[i] == '"' and not key_active and not key_filled: 
            #print("Found key start!")
            key_active = True
            continue
        elif data[i] == '"' and key_active and not key_filled: 
            #print("Found key end!") 
            key_filled = True 
            print(key) 
        elif data[i] == '"' and key_active and key_filled and not value_active: 
            #print("Found value start!")
            value_active = True 
            continue 
        elif data[i] == '"' and key_active and key_filled and value_active: 
            #print("Found value end!")
            key_active = False
            key_filled = False 
            value_active = False 
            print(value)
            final[key] = value 
            value = ''
            key = ''
        elif data[i] == '{': 
            print("Found possible Dict begin")
            new_list = {} 
            final[key] = new_list
            temp = final 
            final = new_list 
            key = value
        elif data[i] == '}': 
            print("Found possible Dict end")
            temp2 = new_list 
            final = temp 
            new_list = temp2 
        elif data[i] == '[': 
            print("Found possible array begin") 
        elif data[i] == ']': 
            print("Found possible array end") 
        
        if (key_active and not key_filled):
            key += data[i]
        elif (key_active and key_filled and value_active): 
            value += data[i] 

'''


class packet: 
    def __init__(self, array, index): 
        self.array = array
        self.index = index 

def parseDict(data, i): 
    key = ""
    value = "" 
    temp = {} 

    Key = True 
    Value = False 

    for j in range(i+1, len(data)): 
        if data[j] == '"': 
            continue 
        elif data[j] == ':': 
            Key = False 
            Value = True
        elif data[j] == ',': 
            temp[key] = value 
            Key = True 
            Value = False
            key = value = ""  

        if data[j] == ',' or data[j] == ':':
            continue 
        if Key and not Value and data[j] != '}': 
            key += data[j]
        elif not Key and Value and data[j] != '}': 
            value += data[j] 
        

        if data[j] == '}':
            temp[key] = value 
            break 
    return packet(temp, j) 

def parseList(data, i): 
    temp = []
    value = "" 
    for j in range(i+1, len(data)): 

        if data[j] == '"': 
            continue 
        elif data[j] == ',': 
            temp.append(value) 
            value = ""

        if data[j] not in [':', ',', '[', ']', '"']: 
            value += data[j] 

        if data[j] == ']': 
            temp.append(value) 
            break 
    return packet(temp, j) 

def load(infile): 
    data = infile.read() 
    start = False 
    final = {}

    key = ""
    value = "" 

    Key = True 
    Value = False 
    i = 1
    while i in range(len(data)): 

        print(data[i], end = '') 

        if data[i] == '{': 
            packet = parseDict(data, i)
            i = packet.index 
            value = packet.array 
            continue 
        elif data[i] == '[': 
            packet = parseList(data, i)
            i = packet.index 
            value = packet.array 
            continue 

        elif data[i] == '"':
            i+=1
            continue 
        elif data[i] == ':': 
            Key = False 
            Value = True 
        elif data[i] == ',':
            final[key] = value 
            Key = False
            Value = True 
            key = ""
            value = None 

        if Key and not Value: 
            key += data[i] 
        elif not Key and Value and value is None: 
            value += data[i] 
            

        i+=1


    return 


load(open(filename, 'r'))



