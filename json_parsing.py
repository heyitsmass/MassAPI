import json 

p = open('output.json', 'r')

output = json.load(p)

search_id = output['searchId']

#print(("Search ID: {}").format(search_id))

results = output['results']

results_terms = {"firstName" : "", "lastName" : "", "address" : "", "city" : "", "state" : "", "zip" : ""}
output_terms = {}

if len(results) > 0: 
    
    #print("More than one result was found")

    for a in results: 
        for key in results_terms:
             results_terms[key] = a[key]  

delim = 'N'

for key in results_terms: 

    temp_key = key 

    res_pos = [i for i, e in enumerate(key+delim) if e.isupper()]
    res_list = [key[res_pos[j]:res_pos[j+1]]
                for j in range(len(res_pos)-1)]

    if len(res_list) > 0: 
        output_terms[key.split(res_list[0])[0].capitalize() + ' ' + res_list[0]] = results_terms[temp_key]
    else:
        output_terms[key.capitalize()] = results_terms[temp_key]

for terms in output_terms: 
    print(terms.ljust(10), ': ', output_terms[terms].ljust(20))
        
p.close() 

