import json
from multiprocessing.sharedctypes import Value 

_filename = "information_sample.json" 
_data = open(_filename, 'r').read() 
#output = json.load(open(_filename, 'r'))

#for key in output: 
#    print(key + ': ' + str(output[key]), str(type(output[key]))) 
print()

def isFloat(input): 
    try: 
        return float(input) 
    except: 
        return False 
    

def checkValue(input): 
    try: 
        return int(input)
    except: 
        pass 

    return isFloat(input) 

def checkType(input):
    # Dictionary of return values 
    return_values = {
        'true': True, 
        'false': False, 
        'null': None
    }

    value = checkValue(input) 
    # Return the adjusted input if its a float, otherwise the input. 
    return value if value else return_values.get(input, input) 

_dict = {} 
_buffer = '' 

for i in range(len(_data)):

    if _data[i] == '{': 
        continue 
    elif _data[i] == '}': 
        break

    _buffer += _data[i] 

_buffer = _buffer.strip('\n').splitlines()W


for word in _buffer: 
    word = word.split(':', 1) 
    for j in range(len(word)): 
        word[j] = word[j].strip("{\n,").lstrip(' "').replace(", ", '').replace('"', '')

    word[1] = checkType(word[1])
    
    _dict[word[0]] = word[1] if len(word) >= 1 else ''  
_buffer = ''     


for key in _dict: 
    print(key + ': ' + str(_dict[key]), str(type(_dict[key]))) 


