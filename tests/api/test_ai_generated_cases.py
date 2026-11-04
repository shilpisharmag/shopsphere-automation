import json
from pathlib import Path
import pytest, requests

BASE_URL = "http://127.0.0.1:5000"

TEST_CASES_PATH = (
    Path(__file__).resolve().parents[2]
     / "data"
    / "generated_test_cases.json"
)


with TEST_CASES_PATH.open(encoding="utf-8") as file:
    generated_data = json.load(file)


@pytest.mark.parametrize("test_case",
                         generated_data["test_cases"],
                         ids=lambda case: case["test_case_id"],)
def test_ai_generated_case(test_case):
    product_id = test_case["input"]["product_id"]
    endpoint = f"{BASE_URL}/product/{product_id}"
    response = requests.get(endpoint, timeout = 10)

    assert response.status_code == test_case["expected_status"]

    actual_response = response.json()
    expected_response = test_case["expected_response"]

    for key, expected_value in expected_response.items():
        if expected_value is not None:
            assert actual_response.get(key)== expected_value