 
class ErrorCode: 
    def __init__(self): 
        pass 

    def http_error(self, e): 
        codes = { 
            400 : 'Bad Request', 
            401 : 'Unauthorized', 
            402 : 'Payment Required', 
            413 : 'Development Bug', 
            500 : 'Internal Server Error', 
            503 : 'Temporarily Unavailable', 
            200 : 'Valid request' 
        }
        
        return codes.get(e, 'Null error') 