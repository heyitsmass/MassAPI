from lxml import html 
import requests 
import json 
import os 
from plugins.json_parser import jsonParser as jp 
from plugins.colors import Colors as color 

def http_error(e): 

    codes = { 
        400 : "Bad request", 
        401 : "Unauthorized", 
        402 : "Payment Required", 
        500 : "Internal Server Error", 
        503 : "Temporarily Unavailable", 
        200 : "Valid request",
    }

    return codes.get(e, "Null Error")

def main():

    os.system('clear')  

    auth_url = "https://api.openpeoplesearch.com/api/v1/User/authenticate"
    auth_data = { "username" : "", "password" : ""}
    auth_headers = { "Content-Type" : "application/json", "accept" : "*/*" }

    search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/PhoneSearch"
    search_data =   '{ "phoneNumber" : "" }'
    search_headers = { "accept" : "text/plain", "Authorization" : "", "Content-Type" : "application/json" }

    auth_response = None 

    auth_data["username"] = input(f"{color.WHT}[{color.RED}-{color.WHT}] Username: {color.RST}")
    os.system('clear')
    print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Username: {color.RST}" + ('*' * int(len(auth_data["username"]) / 2)))

    auth_data["password"] = input(f"{color.WHT}[{color.RED}-{color.WHT}] Password: {color.RST}") 
    os.system('clear')
    print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Username: {color.RST}" + ('*' * int(len(auth_data["username"]) / 2)))
    print(f"{color.WHT}[{color.GRN}✓{color.WHT}] Password: {color.RST}" + ('*' * int(len(auth_data["password"]) / 2)))

    try: 
        auth_response = requests.post(auth_url, headers=auth_headers, data=json.dumps(auth_data)) 

        if auth_response.status_code != 200: 
            raise Exception(http_error(auth_response.status_code)) 

        print(f"{color.WHT}[{color.GRN}+{color.WHT}] User sucessfully authenticated.{color.RST}")  
        
    except Exception as e: 
        print(f"{color.WHT}[{color.RED}X{color.WHT}] Error: {color.RED}" + str(e) + color.RST)

    auth_data["username"] = '-' 
    auth_data["password"] = '-' 

    print(f"{color.WHT}[{color.GRN}✓{color.WHT}] User information redacted sucessfully.{color.RST}")

    return 

if __name__ == "__main__": 
    main() 

#try: 

#   search_headers["Authorization"] = ("Bearer {}").format(auth_response.json()["token"]) 

#   search_response = requests.post(search_url, headers= search_headers, data = search_data)

#   if search_response.status_code != 200: 
#        raise Exception(http_error(search_response.status_code))

#    filename = (search_response.json()["searchId"] + ".json") 
    
#    with open(filename, 'w') as output_file: 
#        json.dump(search_response.json(), output_file)


        
    # p_info[0] = search_response.json()["lastName"] 

    # print("Search Cost ($): {}\n Search Date: {}\n First Name: {}\nLast Name: {}\nAddress: {}\nCity: ()\nState: {}\nZip Code: {}").format(p_info[0], p_info[1], p_info[2], p_info[3], p_info[4], p_info[5], p_info[6], p_info[7])

#except Exception as e: 
#    print(("Error: {}").format(e)) 







