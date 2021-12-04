from lxml import html 
import requests 
import json

auth_url     = "https://api.openpeoplesearch.com/api/v1/User/authenticate"
auth_data    = '{ "username" : "brandon.cannon88@gmail.com", "password" : "CnG2wDfE3789!"}'
auth_headers = { "Content-Type" : "application/json", "accept" : "*/*" }

search_url = "https://api.openpeoplesearch.com/api/v1/Consumer/PhoneSearch"
search_data =   '{ "phoneNumber" : "4259238226" }'
search_headers = { "accept" : "text/plain", "Authorization" : "", "Content-Type" : "application/json" }


auth_response = None

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

search_terms = {"searchCost", "searchDate" }
results_terms = {"firstName", "lastName", "address", "city", "state", "zip" }
response_terms = {"Cost: ", "Date: ", "First Name: ", "Last Name: ", "Address: ", "City: ", "State: ", "Zip Code: "}


try: 
    
    auth_response = requests.post(auth_url, headers = auth_headers, data = auth_data)

    if auth_response.status_code != 200: 
        raise Exception(http_error(auth_response.status_code))

    auth_token = auth_response.json()["token"]

    search_headers["Authorization"] = ("Bearer {}").format(auth_token) 

    search_response = requests.post(search_url, headers= search_headers, data = search_data)

    if search_response.status_code != 200: 
        raise Exception(http_error(search_response.status_code))
    
    print("Output the entire Json to a file? (Y/N): ", end = '')

    if input() == 'Y': 
        print("Input a filename (******.json): ", end = '') 
        filename = input() 
        with open(filename, 'w') as output_file: 
            json.dump(search_response.json(), output_file)
    elif 'N': 

        for terms in response_terms: 
            print(terms, end = ': ') 
    # p_info[0] = search_response.json()["lastName"] 

    # print("Search Cost ($): {}\n Search Date: {}\n First Name: {}\nLast Name: {}\nAddress: {}\nCity: ()\nState: {}\nZip Code: {}").format(p_info[0], p_info[1], p_info[2], p_info[3], p_info[4], p_info[5], p_info[6], p_info[7])

except Exception as e: 
    print(("Error: {}").format(e)) 







