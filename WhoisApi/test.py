filename = "information_sample.json" 
data = open(filename, 'r').read() 

json = {} 

buffer = '' 

i = 0 
while i < len(data):
    if data[i] == ',': 
        break 
    buffer += data[i] 
    i+=1 

buffer = buffer.split(': ', 1)

for i in range(len(buffer)):
    buffer[i] = str(buffer[i].strip('"'), )

json[buffer[0]] = buffer[1]   

print(json) 


buffer = '' 

hello = "hello"

print(hello) 



class J: 
    def __init__(self): 
        pass 

    



