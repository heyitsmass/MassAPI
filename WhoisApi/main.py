import json 
import requests
import tempfile 
import os 

token = None 

TOKEN_PATH = os.path.join(tempfile.gettempdir(), 'mass api') 

if not os.path.isdir(TOKEN_PATH): 
    os.mkdir(TOKEN_PATH) 

TOKEN_PATH = os.path.join(TOKEN_PATH, 'whois.token') 

if os.path.isfile(TOKEN_PATH): 
    with open(TOKEN_PATH, 'r') as in_file: 
        token = in_file.read() 
else: 
    token = input('Enter auth token: ')
    with open(TOKEN_PATH, 'w') as out_file: 
        out_file.write(token) 

# WhoIs Domain Information 

information_link = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey="

information_link += (str(token) + "&domainName=") 

domainName = input("Input Domain/Ipv4/Ipv6/Email Address: ")

information_link += (str(domainName) + "&outputFormat=JSON") 

output = requests.post(information_link)

filename = "information.json" 

with open(filename, 'w') as output_file: 
    output_file.write(output.content.decode()) 


# WhoIs GeoLocation 

geolocation_link = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey="

geolocation_link += (str(token) + "&ipAddress=")

ipAddress = input("Input Ipv4/Ipv6 Address: ")

geolocation_link += str(ipAddress)

filename = "geolocation.json"

output = requests.get(geolocation_link)

with open(filename, 'w') as output_file: 
    output_file.write(output.content.decode())

#DNS Backtrace

dnsbacktrace_link = "https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey="


dnsbacktrace_link += (str(token) + "&domainName=")
domainName = input("Enter Domain Name: ")
dnsbacktrace_link += (str(domainName) + "&type=") 
info_type = input("Input Type (_all for all): ")
dnsbacktrace_link += (str(info_type) + "&outputFormat=JSON")

output = requests.post(dnsbacktrace_link) 

filename = "dnsinformation.json"

output = requests.post(dnsbacktrace_link) 

with open(filename, 'w') as output_file: 
    output_file.write(output.content.decode())
