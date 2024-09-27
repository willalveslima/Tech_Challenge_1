import unittest
import pandas as pd
from app.utils import ler_base_dados_csv, convertar_para_json
from unittest.mock import patch, mock_open

class TestUtils(unittest.TestCase):

    @patch('app.utils.pd.read_csv')
    def test_ler_base_dados_csv(self, mock_read_csv):
        # Mock the return value of pd.read_csv
        mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_read_csv.return_value = mock_df

        url = 'http://example.com/test.csv'
        result = ler_base_dados_csv(url)

        # Assert that pd.read_csv was called with the correct URL
        mock_read_csv.assert_called_once_with(url)
        # Assert that the result is the mocked DataFrame
        pd.testing.assert_frame_equal(result, mock_df)

    def test_convertar_para_json(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        expected_json = '[{"col1":1,"col2":3},{"col1":2,"col2":4}]'

        result = convertar_para_json(df)

        # Assert that the JSON output is as expected
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()