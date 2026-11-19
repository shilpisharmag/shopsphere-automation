
You are an experienced API test automation engineer.

Generate API test scenarios based only on the requirement provided below.

Generate exactly 5 test cases. Generate one and only one test case for each
scenario below, in the listed order:

1. Existing product ID: use only an ID explicitly confirmed as existing
   in the requirement.
2. Non-existing numeric product ID: use a numeric ID explicitly confirmed
   as non-existing. If none is provided, use a reasonable numeric candidate
   but do not invent its expected response data.
3. Non-integer product ID: use a string such as "abc".
4. Product ID 0: test the zero boundary.
5. Negative product ID: use a negative integer such as -1.

Do not omit, combine, duplicate, or replace any scenario.
The test_cases array must contain exactly 5 objects.

Return all five cases inside the "test_cases" array.
Do not return a single test case object.

Rules:
- Generate positive, negative, and boundary test scenarios where applicable.
- Do not invent product names, prices, stock values, IDs, or other response data.
- Do not invent expected response messages.
- Do not assume API behavior that is not stated in the requirement.
- For each test case, provide the test case ID, title, HTTP method, endpoint, input parameters, expected HTTP status, and test type.
- For expected response data, use null when the exact value is not specified by the requirement.
- Return only valid JSON matching the supplied schema.
- Do not assume that a numeric product ID exists.
- For IDs not explicitly confirmed to exist, use expected_status 404.
- Do not classify a large numeric ID as valid unless the requirement confirms it exists.
- For non-integer IDs, use the documented API behavior. If the exact error message is not specified, use null for the error field.
- Do not invent error messages.
- Boundary scenarios must describe the input boundary, not assume a successful response.
- For non-integer IDs and negative IDs, do not assume the error message.Use null for the expected_response.error field unless the requirement, explicitly specifies the message.

IMPORTANT:
- Product ID 1 is an existing product in the ShopSphere database.
- Use product ID 1 for the positive test case.
- Do not generate random product IDs for positive scenarios.
- Do not assume any other product ID exists unless explicitly
  confirmed by the requirement.

Requirement:
{{requirement}}
