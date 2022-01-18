_filename = "information_sample.json" 
_data = open(_filename, 'r').read() 
import json 


#output = json.load(open(_filename, 'r'))

#for key in output: 
#    print(key + ': ' + str(output[key]), str(type(output[key]))) 

_dict = {} 
_buffer = '' 

for i in range(len(_data)):

    if _data[i] == '{': 
        continue 
    elif _data[i] == '}': 
        break

    _buffer += _data[i] 

_buffer = _buffer.strip('\n').splitlines()

def isFloat(input): 
    if '.' in input:        # Refuse a check if the number contains no decimal 
        isFloat = False  
        for i in range(len(input)): 
            if input[i] == '.': 
                if isFloat:         # Refuse values with multiple decimal points 
                    return False 
                isFloat = True
                continue 
            elif not input[i].isnumeric():      # Refuse other non-numeric values 
                return False   
        return float(input)     # Return the type adjusted float value 
    else: 
        return False        # Return false otherwise 

def check_type(input): 
    match input: 
        case 'true': 
            return True 
        case 'false': 
            return False 
        case 'null': 
            return None
        case _: 
            if input.isnumeric(): 
                return int(input)

            is_float = isFloat(input) 
            return is_float if is_float else input  
 

for word in _buffer: 
    word = word.split(':', 1) 
    for j in range(len(word)): 
        word[j] = word[j].strip("{\n,").lstrip(' "').replace(", ", '').replace('"', '')

    word[1] = check_type(word[1]) 
    
    _dict[word[0]] = word[1] if len(word) >= 1 else ''  
_buffer = ''     

for key in _dict: 
    print(key + ': ' + str(_dict[key]), str(type(_dict[key]))) 


