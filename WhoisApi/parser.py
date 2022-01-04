import json

LENGTH_LIMIT = 35

def parse(numTabs=0, List=[], output=None): 

    delim = " "

    for key in output: 
        try: 
            if len(output[key]) > LENGTH_LIMIT: 
                output[key] = "******* Check output file *******"
        except TypeError: 
            pass 

        for letter in key: 
            if letter.isupper(): 
                delim = letter
                break 

        new_key = key.split(delim) 

        
        if type(output[key]) != list and type(output[key]) != dict: 
            addition = (" " + delim + new_key[1] + ": " + str(output[key])) if len(new_key) > 1 else (": " + str(output[key])) 
        else: 
            addition = (" " + delim + new_key[1] + ": ") if len(new_key) > 1 else ": "

        List.append(("\t" * numTabs) + new_key[0].capitalize() + addition)

        numTabs += 1

        if type(output[key]) is list:  
            parseArray(numTabs, List, output[key]) 
        elif type(output[key]) is dict:
            parse(numTabs, List, output[key])           

        numTabs -= 1

    return List

def parseArray(numTabs, List, output=None): 
    for index in range(len(output)): 
        if type(output[index]) is dict: 
            parse(numTabs, List, output[index])
        else:
            if len(str(output[index])) > LENGTH_LIMIT: 
                output[index] = "******* Check output file *******"      
            List.append(("\t" * numTabs) + str(output[index]))
    return 

def load(filename = ""): 
    try: 
        return parse(output=json.load(open(filename, 'r')))
    except OSError as e: 
        print(e) 
    return None

output = load("geolocation.json") 

for word in output: 
    print(word) 

