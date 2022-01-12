filename = "geolocation.json" 

class package: 
    def __init__(self, data, i=0): 
        self.data = data 
        self.index = i 

def load_arr(data, i=1, json={}): 

    string = "" 
    arr = [] 

    while i < len(data):
        if data[i] == '{': 
            packet = load_dict(data, i+1, json)
            i = packet.index
            arr.append(packet.data)
            continue 
        if data[i] == ']':
            string = string.split(',')
            for j, k in enumerate(string, 0): 
                string[j] = k.strip() 
                string[j] = string[j].replace('"', '') 
                if len(string[j]) > 0: 
                    arr.append(string[j]) 
            break 

        if data[i] not in ['\n']: 
            string += data[i] 

        i+=1 
    return package(arr, i+1) 


# Problem
# This will only properly parse dictionaries when the dict is formatted like so 
#   { "Title":{ 
#           "key1" : "value1", 
#           "key2" : {
#                   "keyA" : "valueA", 
#                   "keyB" : "valueB", 
#                   ...
#               }, 
#           , 
#       }
# }
# Reason
# Any dictionary formatted like so is improperly parsed and returned
#   { "key1" : "value1", 
#     "key2" : { 
#           "keyA" : "valueA", 
#           ...
#       }, 
#      "key3" : "value3", 
#      ....
# }
#

def load_dict(data, i=1, json={}, head='', saved_key='', final={}): 
    string = key = ''
    temp = {} 
    while i < len(data):
         
        if data[i] in ['{', '}', '[']:
            if type(string) == str: 
                string = string.splitlines()

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

            string = "" 

            if data[i] == '{':
                if head == '': 
                    head = key 

                packet = load_dict(data, i+1, json, head, key)
                i = packet.index

                if key != head:  
                    temp[key] = packet.data
                else: 
                    for key in packet.data: 
                        json[key] = packet.data[key] 

                if saved_key == head: 
                    for key in temp: 
                        json[key] = temp[key]      

                if i < len(data)-1: 
                    continue 
                else:
                    final[head] = json 
                    break 

            elif data[i] == '}': 

                return package(temp, i+1)

            elif data[i] == '[':
                #print(temp, '\n') 
                packet = load_arr(data, i+1, json)
                i = packet.index
                temp[key] = packet.data
                continue 

            elif data[i] == '\n':

                i+=1
                continue

        string += data[i]
        i+=1

    return package(final, i+1) 


def load(infile): 

    return load_dict(infile.read()).data

output = load(open(filename, 'r')) 

print(output) 
