import json 

_filename = "information_sample.json" 
_data = open(_filename, 'r').read() 
#output = json.load(open(_filename, 'r'))

#for key in output: 
#    print(key + ': ' + str(output[key]), str(type(output[key]))) 
print()

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
    # Refuse a check if the number contains no decimal 
    if '.' in input:         
        isFloat = False
        isNegative = False  
        for i in range(len(input)): 
            if input[i] == '.':
                # Refuse values with multiple decimal points 
                if isFloat:          
                    return False 
                isFloat = True
                continue
            elif input[i] == '-': 
                # Refuse values with negatives in the middle (1.32-04)
                if not isNegative and i > 0 or isNegative:
                    return False
                elif not isNegative and i == 0:
                    isNegative = True 
                    continue 
            elif not input[i].isnumeric():
                return False 
        return float(input) 
    # Return false otherwise 
    return False

def isScientific(input): 
    if 'e' not in input:
        if 'E' not in input:  
            return False 

    isExponent = isNegative = negativeExponent = False
 
    for i in range(len(input)): 
        if not input[i].isnumeric(): 
            if input[i] not in ['e', 'E', '.', '-']: 
                return False
            if input[i].lower() == 'e' and not isExponent: 
                isExponent = True
            elif input[i].lower() == 'e' and isExponent:
                return False
            
            if input[i] == '-' and not isNegative: 
                isNegative = True 
            # Reject value with more than two '-'
            elif input[i] == '-' and isNegative and not negativeExponent:
                if i > 1: 
                    # Verify proper notation '1.0E-12'
                    print(input[i-1].lower()) 
                    if input[i-1].lower() == 'e':
                        negativeExponent = True
                        continue 
                    return False 
                # Reject improper values '1.-0E2'
                else:  
                    return False
            elif input[i] == '-' and isNegative and negativeExponent: 
                return False 

    return float(input)  



def check_number(input):
    # Check if the number is a float
    is_float = isFloat(input) 
    if is_float: 
        return is_float 
    
    is_scientific = isScientific(input)
    if is_scientific: 
        return is_scientific
    # Check if the number is negative 
    if input[0] == '-':
        # Convert the value if an int is found after stripping the negative 
        return int(input) if input.lstrip('-').isnumeric() else False
    # Otherwise check if the number is numeric and return the converted value
    return int(input) if input.isnumeric() else False 


def check_type(input):
    # Dictionary of return values 
    return_values = {
        'true': True, 
        'false': False, 
        'null': None
    }

    value = check_number(input) 
    # Return the adjusted input if its a float, otherwise the input. 
    return value if value else return_values.get(input, input) 


for word in _buffer: 
    word = word.split(':', 1) 
    for j in range(len(word)): 
        word[j] = word[j].strip("{\n,").lstrip(' "').replace(", ", '').replace('"', '')

    word[1] = check_type(word[1])
    
    _dict[word[0]] = word[1] if len(word) >= 1 else ''  
_buffer = ''     


for key in _dict: 
    print(key + ': ' + str(_dict[key]), str(type(_dict[key]))) 


