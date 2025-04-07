import unittest
from unittest.mock import patch
import pandas as pd
from uber_pickups import load_data, DATE_COLUMN, DATA_URL

# Mock the Streamlit cache_data decorator to avoid Streamlit-specific warnings
@patch('streamlit.cache_data', lambda func: func)
class TestUberPickups(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_load_data(self, mock_read_csv):
        """
        Test the load_data function to ensure it processes data correctly.
        """
        # Mock data to simulate the dataset
        mock_data = pd.DataFrame({
            'date/time': ['2025-04-07 10:00:00', '2025-04-07 11:00:00'],
            'value': [1, 2]
        })
        mock_read_csv.return_value = mock_data

        # Call the function with a mock number of rows
        result = load_data(2)

        # Check if the read_csv function was called with the correct URL and nrows
        mock_read_csv.assert_called_once_with(DATA_URL, nrows=2)

        # Verify the column names are converted to lowercase
        self.assertIn('date/time', result.columns)
        self.assertIn('value', result.columns)

        # Verify the date/time column is converted to datetime
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result[DATE_COLUMN]))

    @patch('pandas.read_csv')
    def test_load_data_empty(self, mock_read_csv):
        """
        Test the load_data function with an empty dataset.
        """
        # Mock an empty DataFrame
        mock_data = pd.DataFrame(columns=['date/time', 'value'])
        mock_read_csv.return_value = mock_data

        # Call the function
        result = load_data(0)

        # Verify the result is an empty DataFrame
        self.assertTrue(result.empty)

if __name__ == '__main__':
    unittest.main()