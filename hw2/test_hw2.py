import pytest
import json
from hw_2 import process_data  # Импортируйте вашу функцию здесь
from datetime import datetime

# Функция для создания тестового файла
def create_test_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

@pytest.mark.parametrize("input_data, expected_output", [
    # Тест 1: Стандартный сценарий
    (
        {'user1': {'age': 20, 'last_login': str(datetime.today().date())}},
        {'age_statistics': {'0-18': 0, '18-25': 100.0, '25-45': 0, '45-60': 0, '60+': 0},
         'time_statictics': {'<2': 100.0, '7': 0, '28-31': 0, '182': 0, '>182': 0}
        }
    ),
    # Добавьте другие тестовые сценарии здесь
])
def test_process_data(tmpdir, input_data, expected_output):
    input_path = tmpdir.join("input.json")
    output_path = tmpdir.join("output.json")

    create_test_file(input_data, input_path)
    process_data(str(input_path), str(output_path))

    with open(str(output_path), 'r') as file:
        output_data = json.load(file)
        assert output_data == expected_output