import json
import pytest
from hw_2 import process_data

# Define test cases with input path, output path, and expected results
TEST_CASES = [
    ("data_hw2.json", "output1.json", {"age_statistics": {'0-18': 50.0, '18-25': 0.0, '25-45': 0.0, '45-60': 50.0, '60+': 0.0}, "time_statistics": {'<2': 0.0, '7': 0.0, '28-31': 0.0, '182': 50.0, '>182': 50.0}}),
    ("test_data.json", "output2.json", {"age_statistics": {'0-18': 0.0, '18-25': 50.0, '25-45': 0.0, '45-60': 50.0, '60+': 0.0}, "time_statistics": {'<2': 0.0, '7': 0.0, '28-31': 0.0, '182': 50.0, '>182': 50.0}}),
    # Add more test cases as needed
]

# Parametrize the test function with input, output, and expected results
@pytest.mark.parametrize("input_path, output_path, expected_result", TEST_CASES)
def test_process_data(input_path, output_path, expected_result, tmp_path):
    # Run the function with a temporary output file in the temporary directory
    process_data(input_path, str(tmp_path / output_path))

    # Load the actual output file
    with open(tmp_path / output_path, "r") as file:
        actual_result = json.load(file)

    # Check age statistics
    for category, expected_percentage in expected_result["age_statistics"].items():
        assert category in actual_result["age_statistics"]
        actual_percentage = actual_result["age_statistics"][category]
        assert pytest.approx(actual_percentage, rel=1e-2) == expected_percentage

    # Check time statistics
    for days, expected_percentage in expected_result["time_statistics"].items():
        assert days in actual_result["time_statistics"]
        actual_percentage = actual_result["time_statistics"][days]
        assert pytest.approx(actual_percentage, rel=1e-2) == expected_percentage

# No need for cleanup in pytest_sessionfinish
