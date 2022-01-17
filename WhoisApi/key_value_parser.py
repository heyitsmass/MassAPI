filename = "information_sample.json" 
data = open(filename, 'r').read() 

_dict = {} 
buffer = '' 

for i in range(len(data)): 
  if data[i] == ',' or data[i] == '}': 
    buffer = buffer.split(':', 1) 
    for j in range(len(buffer)): 
      buffer[j] = buffer[j].strip("{\n").lstrip(" ,\n").replace('"', '')
    _dict[buffer[0]] = buffer[1] 
    buffer = '' 
  buffer += data[i] 
  i+=1