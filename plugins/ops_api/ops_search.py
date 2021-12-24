from .ops_response import Response
from .ops_banner import Banner

class Search(object): 
    def __init__(self, scr, token):
        self.auth_token = token 
        self.window = scr
    
    def phone(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['phone search']) 
        searchType = 'PhoneSearch'
        args = [{
            'phoneNumber' : ''
        }, {
            '[X] Enter phone number:' : 'phoneNumber' 
        }]

        return Response(self.window).getResponse(args, searchType, self.auth_token) 

    
    def email(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['email search'])
        searchType = 'EmailAddressSearch'
        args = [{
            'emailAdress' : ''
        }, {
            '[X] Enter email address:' : 'emailAddress'
        }]        

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def name(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name search']) 
        searchType = 'NameSearch'
        args = [{
            'firstName' : '', 
            'middleName' : '', 
            'lastName' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter first name (required):' : 'firstName' ,
            '[X] Enter middle name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter city (optional):' : 'city',
            '[X] Enter state (optional):' : 'state'   

        }]

        'firstName'     #Partial okay
        'middleName'    #Opt 
        'lastName' 
        'city'          #Opt
        'state'         #Opt

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def nameAddress(self): 
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name address search']) 
        searchType = 'NameAddressSearch'
        args = [{ 
            'firstName' : '',#Opt
            'lastName' : '',
            'address' : '', 
            'unit'   : '',   #Opt
            'city' : '',
            'state' : ''
        }, { 
            '[X] Enter first name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter address (required):' : 'address',
            '[X] Enter unit # (optional):' : 'unit',   
            '[X] Enter city (required):' : 'city',
            '[X] Enter state (required):' : 'state'       
        }]

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def nameDOB(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['name dob search']) 
        searchType = 'nameDOBSearch'
        args = [{
            'firstName' : '', 
            'lastName' : '', 
            'dob' : ''
        }, {
            '[X] Enter first name (optional):' : 'firstName' , 
            '[X] Enter last name (required):' : 'lastName',
            '[X] Enter DOB (required):' : 'dob'
        }]

        'firstName' #partial okay
        'lastName' 
        'dob'       # DD/MM/YYY or 00/00/YYY

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def business(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['business search']) 
        searchType = 'BusinessSearch'
        args = [{
            'businessName' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter Business Name (required):' : 'businessName', 
            '[X] Enter city (optional):' : 'city', 
            '[X] Enter state (optional):' : 'state'          
        }]

        'businessName' 
        'city' #Opt
        'state' #Opt    
        #City/State or State

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def address(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['address search']) 
        searchType = 'AddressSearch'
        args = [{
            'address' : '', 
            'unit' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter Address (required):' : 'address', 
            '[X] Enter unit (optional):' : 'unit', 
            '[X] Enter city (required):' : 'city', 
            '[X] Enter state (required):' : 'state'
        }]

        return Response(self.window).getResponse(args, searchType, self.auth_token)

    def poBox(self):
        Banner.display_banner(self)  
        self.window.addstr(8, 46, Banner.sub_banners['pobox search'])
        searchType = 'PoBoxSearch'
        args = [{
            'poBox' : '', 
            'city' : '', 
            'state' : ''
        }, {
            '[X] Enter PO Box (required):' : 'poBox', 
            '[X] Enter City (required):' : 'city', 
            '[X] Enter State (required):' : 'state'
        }]

        return Response(self.window).getResponse(args, searchType, self.auth_token)
