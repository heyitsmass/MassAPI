import json 
from io import StringIO

output = "Hello World" 

p = open('output.json', 'r')

output = json.load(p)

results = output['results']

results_terms = {"firstName" : "", "lastName" : "", "address" : "", "city" : "", "state" : "", "zip" : ""}

if len(results) > 0: 
    print("More than one result was found")


    for a in results: 
        for key in results_terms:
             results_terms[key] = a[key]   

    print(results_terms) 

for key in results_terms:
    print(key, "%2d"

p.close() 

