

GENERTATED_TESTCASE_SCHEMA = {
       "type": "object",
       "properties": {
           "test_cases": {
               "type": "array",
               "items":{
                   "type": "object",
                   "Properties":{
                       "test_case_id": {
                           "type" : "String"
                       },
                       "title":{
                           "type": "String"
                       },
                       "method" : {
                           "type" : "string",
                           "enum" : ["GET"]
                       },
                       "endpoint":{
                           "type" : "string",
                       },
                       "input" : {

                           "type" : "object",
                           "properties" : {
                               "product_id" : {
                                   "type" : ["integer", "String"]
                               }
                           }
                       },
                       "required" : ["product_id"],
                       "additional_properties" : False
                   },
                   "expected_status": {
                       "type" : "integer",
                       "enum" : [200,404]
                   },
                   "expected_response" : {
                       "type" : "object"
                   },
                   "test_type" : {
                       "type" : "string",
                       "enum" : ["positive", "negative", "boundary"]
                   }
               },
               "required":[
                   "test_case_id",
                   "title",
                   "method",
                   "endpoint",
                   "input",
                   "expected_status",
                   "expected_response",
                   "test_type"
               ],
               "additionalProperties" : False
           }
       },
       "required": ["test_cases"],
       "additionalProperties": False

}