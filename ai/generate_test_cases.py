from ai.generate_prompt_locally import load_generation_prompt
import json
from openai import OpenAI
from data.schemas.generated_test_cases_schema import GENERTATED_TESTCASE_SCHEMA
from pathlib import Path


MODEL= "gpt-4o-mini"

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
    print(json.dumps(test_cases, indent=2))
    # genertatedTestcases = json.dumps(test_cases, indent=2)
    OUTPUT_PATH = Path("data/generated_test_cases.json")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(test_cases, file, indent=2)
    print(f"Test cases saved to: {OUTPUT_PATH}")

