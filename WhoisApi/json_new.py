# Problem
# We can parse dictionaries when it is formatted like so 
#   { "Title":{ 
#           "key1" : "value1", 
#           "key2" : {
#                   "keyA" : "valueA", 
#                   "keyB" : "valueB", 
#                   ...
#               }, 
#           , 
#       }
# }
# Reason
# Any dictionary formatted like so is improperly parsed and returned
#   { "key1" : "value1", 
#     "key2" : { 
#           "keyA" : "valueA", 
#           ...
#       }, 
#      "key3" : "value3", 
#      ....
# }




