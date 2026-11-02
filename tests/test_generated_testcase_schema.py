import pytest
from data.schemas.generated_test_cases_schema import GENERTATED_TESTCASE_SCHEMA
from jsonschema import validate, ValidationError


def test_valid_generated_testcase_matches_schema():
    generated_output = {
        "test_cases" :[
            {
                "testcase_id": 101,
                "title": "Retrieve an existing product",
                "method": "GET",
                "endpoint": "/product/1",
                "input": {
                    "product_id": 1
                },
                "expected_status": 200,
                "expected_response": {
                    "id": 1,
                    "name": "Laptop",
                    "price": 75000,
                    "stock": 10
                },
                "test_type": "positive"

            }
        ]
    }

    validate(instance = generated_output, schema=GENERTATED_TESTCASE_SCHEMA)

def test_schema_rejects_missing_test_case_id():
        invalid_output = {
              "testcases" : [
                    {
                           "title": "Retrieve an existing product",
                            "method": "GET",
                            "endpoint": "/product/1",
                            "input": {
                            "product_id": 1
                            },
                            "expected_status": 200,
                            "expected_response": {
                            "id": 1,
                            "name": "Laptop",
                            "price": 75000,
                            "stock": 10
                            },
                            "test_type": "positive"
                    }
              ]
        }
        with pytest.raises(ValidationError):
              validate(instance = invalid_output, schema=GENERTATED_TESTCASE_SCHEMA)