from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQUIREMENT_PATH = (PROJECT_ROOT / "requirements" / "get_product_by_id.md")

PROMPT_PATH = (PROJECT_ROOT / "ai" / "prompts" / "test_case_generation_prompt.md")


def load_generation_prompt():
    """
    Load the API requirement and insert it into the prompt template.
    """

    requirement = REQUIREMENT_PATH.read_text(encoding="utf-8")
    prompt_template = PROMPT_PATH.read_text(encoding="utf=8")

    prompt = prompt_template.replace("{{requirement}}", requirement)
    return prompt


if __name__ == "__main__":
    prompt = load_generation_prompt()
    print("Prompt loaded successfuly.")
    print("-" * 50)
    print(prompt)