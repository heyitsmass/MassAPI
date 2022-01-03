import json
from typing import Type 

LENGTH_LIMIT = 35

def parse(output=None, numTabs=0, List=[]): 

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
            if len(new_key) > 1: 
                addition = ' ' + delim + new_key[1] + ': ' + str(output[key]) 
            else: 
                addition = ': ' + str(output[key]) 
        else: 
            if len(new_key) > 1: 
                addition = ' ' + delim + new_key[1] + ': '
            else: 
                addition = ': '

        List.append(("\t" * numTabs) + new_key[0].capitalize() + addition)

        numTabs += 1

        if type(output[key]) is list:  
            parseArray(numTabs, List, output[key]) 
        elif type(output[key]) is dict:
            parse(output[key], numTabs, List)

        numTabs -= 1

    return List

def parseArray(numTabs, List, output=None): 
    for index in range(len(output)): 
        if type(output[index]) is dict: 
            parse(output[index], numTabs, List) 
        else:
            if len(str(output[index])) > LENGTH_LIMIT: 
                output[index] = "******* Check output file *******"      
            List.append(("\t" * numTabs) + str(output[index]))
    return 

def load(filename = ""): 
    try: 
        return parse(json.load(open(filename, 'r')))
    except OSError as e: 
        print(e) 
    return None

output = load("information.json") 



for word in output: 
    print(word) 

