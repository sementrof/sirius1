import json
import pytest
import os
from hw_2 import process_data

TEST_CASES = [
    ("data_hw2.json", "output_1.json", {"age_statistics": {'0-18': 50.0, '18-25': 0, '25-45': 0, '45-60': 50.0, '60+': 0}, "time_statictics": {'<2': 0, '7': 0.0, '28-31': 0.0, '182': 50.0, '>182': 50.0}}),
    ("test_data.json", "output_2.json", {"age_statistics": {"0-18": 0, "18-25": 50.0, "25-45": 0, "45-60": 50.0, "60+": 0}, "time_statictics": {"<2": 0, "7": 0, "28-31": 0, "182": 50.0, ">182": 50.0}}),
]

@pytest.mark.parametrize("input_filename, output_filename, expected_result", TEST_CASES)
def test_process_data(input_filename, output_filename, expected_result):
    input_path = os.path.join( input_filename)
    output_path = os.path.join(output_filename)

    process_data(input_path, output_path)

    with open(output_path, "r") as file:
        actual_result = json.load(file)

    for category, expected_percentage in expected_result['age_statistics'].items():
        assert category in actual_result['age_statistics']
        actual_percentage = actual_result['age_statistics'][category]
        assert actual_percentage == expected_percentage

    for days, expected_percentage in expected_result['time_statictics'].items():
        assert days in actual_result['time_statictics']
        actual_percentage = actual_result['time_statictics'][days]
        assert actual_percentage == expected_percentage

    os.remove(output_path)

# Additional Test Cases

def test_process_data_empty_input():
    input_filename = "data_hw2.json"
    output_filename = "output_empty.json"
    input_path = os.path.join( input_filename)
    output_path = os.path.join( output_filename)

    process_data(input_path, output_path)

    with open(output_path, "r") as file:
        actual_result = json.load(file)

    # Add assertions for the expected output based on an empty input

    os.remove(output_path)

def test_process_data_invalid_input():
    input_filename = "test_data.json"
    output_filename = "output_invalid.json"
    input_path = os.path.join( input_filename)
    output_path = os.path.join(output_filename)

    process_data(input_path, output_path)

    with open(output_path, "r") as file:
        actual_result = json.load(file)

    # Add assertions for the expected output based on invalid input

    os.remove(output_path)
