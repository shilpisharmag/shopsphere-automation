
def validate_test_cases(test_cases):
    """
    Perform semantic validation of AI-generated ShopSphere API test cases.
    """

    cases = test_cases.get("test_cases", [])

    if len(cases) != 5:
        raise ValueError(
            f"Expected exactly 5 test cases, received {len(cases)}"
        )

    test_case_ids = set()
    covered_scenarios = set()

    required_scenarios = {
        "existing_product",
        "non_existing_numeric",
        "non_integer",
        "zero_boundary",
        "negative_boundary"
    }

    for case in cases:

        test_case_id = case["test_case_id"]
        product_id = case["input"]["product_id"]

        # 1. Validate unique test case IDs
        if test_case_id in test_case_ids:
            raise ValueError(
                f"Duplicate test case ID: {test_case_id}"
            )

        test_case_ids.add(test_case_id)

        # 2. Validate HTTP method
        if case["method"] != "GET":
            raise ValueError(
                f"{test_case_id}: Expected GET method"
            )

        # 3. Validate endpoint consistency
        expected_endpoint = f"/product/{product_id}"

        if case["endpoint"] != expected_endpoint:
            raise ValueError(
                f"{test_case_id}: Expected endpoint {expected_endpoint}"
            )

        # 4. Identify scenario from input
        if isinstance(product_id, str):
            if product_id != "abc":
                raise ValueError(
                    f"{test_case_id}: Unexpected non-integer input"
                )

            scenario = "non_integer"
            expected_status = 404
            expected_type = "negative"

        elif isinstance(product_id, int) and not isinstance(product_id, bool):

            if product_id == 1:
                scenario = "existing_product"
                expected_status = 200
                expected_type = "positive"

            elif product_id > 1:
                scenario = "non_existing_numeric"
                expected_status = 404
                expected_type = "negative"

            elif product_id == 0:
                scenario = "zero_boundary"
                expected_status = 404
                expected_type = "boundary"

            elif product_id == -1:
                scenario = "negative_boundary"
                expected_status = 404
                expected_type = "boundary"

            else:
                raise ValueError(
                    f"{test_case_id}: Unsupported product ID {product_id}"
                )

        else:
            raise ValueError(
                f"{test_case_id}: Invalid product ID type"
            )

        # 5. Validate expected status
        if case["expected_status"] != expected_status:
            raise ValueError(
                f"{test_case_id}: Expected status {expected_status}, "
                f"got {case['expected_status']}"
            )

        # 6. Normalize test type using scenario rules
        case["test_type"] = expected_type

        # 7. Validate positive response ID
        if scenario == "existing_product":
            expected_id = case["expected_response"].get("id")

            if expected_id not in (None, 1):
                raise ValueError(
                    f"{test_case_id}: Expected response ID must be 1"
                )

            case["expected_response"]["id"] = 1

        # 8. Detect duplicate scenarios
        if scenario in covered_scenarios:
            raise ValueError(
                f"Duplicate scenario detected: {scenario}"
            )

        covered_scenarios.add(scenario)

    # 9. Validate complete scenario coverage
    missing_scenarios = required_scenarios - covered_scenarios

    if missing_scenarios:
        raise ValueError(
            f"Missing required scenarios: {missing_scenarios}"
        )

    print("Semantic validation passed.")
    print("Covered scenarios:", sorted(covered_scenarios))

    return True
