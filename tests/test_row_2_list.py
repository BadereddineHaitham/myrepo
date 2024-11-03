import csv
from row_2_list import row_to_list  # Import the function to be tested
import pytest

# Load your dataset from the CSV file
dataset = []
with open('data/house_price.csv', 'r') as csvfile:  # Ensure path is correct
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    input_string = ' '.join(input_row)  # Convert list to string
    result = row_to_list(input_string)  # Apply the function to get a list
    
    # Assert to check for missing values
    assert all(value != '' for value in result), "Row contains missing values"
