from ai.generate_prompt_locally import load_generation_prompt
import json
from openai import OpenAI
from data.schemas.generated_test_cases_schema import GENERTATED_TESTCASE_SCHEMA
from pathlib import Path
from ai.validate_test_cases import validate_test_cases


MODEL= "gpt-4o-mini"

def normalize_test_cases(test_cases):
    """
    Normalize generated cases where the requirement does not
    specify an exact error message.
    """

    for test_case in test_cases.get("test_cases", []):
        product_id = test_case.get("input",{}).get("product_id")
        # Non-integer and negative IDs may trigger Flask's
        # default 404 response. The exact message is not
        # specified in the requirement.

        expected_response = test_case.setdefault(
            "expected_response", {}
        )

        if product_id == 1:
            expected_response["id"] = 1

        if isinstance(product_id, str) or (
            isinstance(product_id, int) and product_id < 0
        ):
            test_case.setdefault("expected_response", {})["error"] = None
    return test_cases

def generate_testcases():
    prompt=load_generation_prompt()
    client=OpenAI()

    response = client.responses.create(
                model=MODEL,
                input=prompt,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "generate_test_cases",
                        "strict": True,
                        "schema": GENERTATED_TESTCASE_SCHEMA
                    }
                },
            )
    if not response.output_text:
        raise RuntimeError("The model return empty error")
    return json.loads(response.output_text)

if __name__ == "__main__":
    test_cases = generate_testcases()

    # Normalize generated test cases
    test_cases = normalize_test_cases(test_cases)
    print("\nGenerated scenario details:")

    for case in test_cases.get("test_cases", []):
        print(
            case["test_case_id"],
            "| Product ID:", repr(case["input"]["product_id"]),
            "| Status:", case["expected_status"],
            "| Type:", case["test_type"]
        )

    # Validate test case count and scenario correctness
    validate_test_cases(test_cases)

    # Display generated test cases
    print(json.dumps(test_cases, indent=2))

    # Save generated test cases
    OUTPUT_PATH = Path("data/generated_test_cases.json")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(test_cases, file, indent=2)

    print(f"Test cases saved to: {OUTPUT_PATH}")

