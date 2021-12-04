from lxml import html

import requests

auth_url = "https://api.openpeoplesearch.com/api/v1/User/authenticate"
search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/PhoneSearch"

auth_headers = { "Content-Type" : "application/json", "accept" : "*/*" }
search_headers = { "accept" : "text/plain", "Authorization" : " ", "Content-Type" : "application/json" }

auth_data =     '{ "username" : "**************", "password" : "**************"}'
search_data =   '{ "phoneNumber" : "**********" }'

filename = "output.json"

auth_response = requests.post(auth_url, headers = auth_headers, data = auth_data)

auth_token = auth_response.json()["token"]

# Authentication has been validated 

search_headers["Authorization"] = ("Bearer {}").format(auth_token) 

search_response = requests.post(search_url, headers = search_headers, data = search_data) 

p = open(filename, 'w') 

p.write(search_response.json())

p.close() 





















