

GENERTATED_TESTCASE_SCHEMA = {
       "type": "object",
       "properties": {
           "test_cases": {
               "type": "array",
               "items":{
                   "type": "object",
                   "properties":{
                       "test_case_id": {
                           "type" : "string"
                       },
                       "title":{
                           "type": "string"
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
                                   "type" : ["integer", "string"]
                               }
                           },
                           "required" : ["product_id"],
                           "additionalProperties" : False
                       },   
                       "expected_status": {
                           "type" : "integer",
                           "enum" : [200,404]
                        },
                        "expected_response" : {
                             "type": "object",
                             "properties": {
                                   "id": {
                                    "type": ["integer", "null"]
                                    },
                                    "name": {
                                      "type": ["string", "null"]
                                     },
                                    "price": {
                                       "type": ["number", "null"]
                                    },
                                    "stock": {
                                        "type": ["integer", "null"]
                                    },
                                     "error": {
                                        "type": ["string", "null"]
                                    }
                                },
                                "required": ["id", "name", "price", "stock", "error"],
                                "additionalProperties": False
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
           }
       },
       "required": ["test_cases"],
       "additionalProperties": False
    }   