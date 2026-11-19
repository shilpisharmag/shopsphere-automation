import json
from pathlib import Path
import pytest, requests
from jsonschema import validate, ValidationError
from data.schemas.product_response_schema import PRODUCT_RESPONSE_SCHEMA
import allure

BASE_URL = "http://127.0.0.1:5001"

TEST_CASES_PATH = (
    Path(__file__).resolve().parents[2]
     / "data"
    / "generated_test_cases.json"
)


with TEST_CASES_PATH.open(encoding="utf-8") as file:
    generated_data = json.load(file)

assert len(generated_data["test_cases"]) == 5, (
    f"Expected 5 test cases, got {len(generated_data['test_cases'])}"
)

@allure.feature("Shopsphere Product API")
@allure.story("Retreive product by product ID")

@pytest.mark.parametrize("test_case",
                         generated_data["test_cases"],
                         ids=lambda case: case["test_case_id"],)
def test_ai_generated_case(test_case):
    product_id = test_case["input"]["product_id"]
    endpoint = f"{BASE_URL}/product/{product_id}"

    allure.dynamic.title(f"{test_case['test_case_id']} - {test_case['title']}")
    allure.dynamic.description(
        f"Scenario: {test_case['test_type']}\n"
        f"Method: {test_case['method']}\n"
        f"Endpoint: {endpoint}\n"
        f"Expected Status: {test_case['expected_status']}"
    )

    allure.dynamic.tag(test_case["test_type"])
    allure.dynamic.severity(
        allure.severity_level.CRITICAL
        if test_case["test_type"] == "positive"
        else allure.severity_level.NORMAL
    )
    with allure.step(f"Send {test_case['method']} request to {endpoint}"):
        response = requests.get(endpoint, timeout = 10)

    with allure.step("Validate HTTP status code"):
        assert response.status_code == test_case["expected_status"]
    # if response.status_code == 200 :
    #     validate(instance=response.json(), schema=PRODUCT_RESPONSE_SCHEMA)

    actual_response = response.json()
    expected_response = test_case["expected_response"]
     
    with allure.step("Validate API response fields"):
        for key, expected_value in expected_response.items():
            if expected_value is not None:
                assert actual_response.get(key)== expected_value