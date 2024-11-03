
import csv
import pytest
from src.utils.row_2_list import row_to_list  # Import the function to be tested

def test_row_to_list_with_tabs_and_newlines():
    input_str = "(2,081\t314,942\n)"
    expected_output = ["(2,081", "314,942)"]
    assert row_to_list(input_str) == expected_output

def test_row_to_list_with_spaces():
    input_str = "Hello World Python"
    expected_output = ["Hello", "World", "Python"]
    assert row_to_list(input_str) == expected_output

def test_row_to_list_empty_string():
    input_str = ""
    expected_output = []
    assert row_to_list(input_str) == expected_output

def test_row_to_list_single_value():
    input_str = "42"
    expected_output = ["42"]
    assert row_to_list(input_str) == expected_output


# Load your dataset from the CSV file
dataset = []
with open('data/house_price.csv', 'r') as csvfile:  # Update with correct path
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    # Convert row to string format expected by row_to_list
    input_string = ' '.join(input_row)
    # Convert string to list using row_to_list function
    result = row_to_list(input_string)
    
    # Assert that no element in the result list is empty (indicating missing values)
    assert all(element.strip() != "" for element in result), "Row contains missing values"


