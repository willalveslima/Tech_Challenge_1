import unittest
import pandas as pd
from app.utils import ler_base_dados_csv, converter_para_json
from unittest.mock import patch, mock_open

class TestUtils(unittest.TestCase):

    class TestUtils(unittest.TestCase):

        @patch('app.utils.pd.read_csv')
        def test_ler_base_dados_csv(self, mock_read_csv):
            # Mock the return value of pd.read_csv
            mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
            mock_read_csv.return_value = mock_df

            url = 'http://example.com/test.csv'
            result = ler_base_dados_csv(url)

            # Assert that pd.read_csv was called with the correct URL
            mock_read_csv.assert_called_once_with(url, sep=";")
            # Assert that the result is the mocked DataFrame
            pd.testing.assert_frame_equal(result, mock_df)

        def test_convertar_para_json(self):
            df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
            expected_json = '[{"col1":1,"col2":3},{"col1":2,"col2":4}]'

            result = converter_para_json(df)

            # Assert that the JSON output is as expected
            self.assertEqual(result, expected_json)

        def test_convertar_para_json_empty_dataframe(self):
            df = pd.DataFrame()
            expected_json = '[]'

            result = converter_para_json(df)

            # Assert that the JSON output is as expected for an empty DataFrame
            self.assertEqual(result, expected_json)

        @patch('app.utils.pd.read_csv')
        def test_ler_base_dados_csv_invalid_url(self, mock_read_csv):
            # Mock pd.read_csv to raise an error
            mock_read_csv.side_effect = Exception("Invalid URL")

            url = 'http://invalid-url.com/test.csv'

            with self.assertRaises(Exception) as context:
                ler_base_dados_csv(url)

            # Assert that the exception message is as expected
            self.assertTrue('Invalid URL' in str(context.exception))

    if __name__ == '__main__':
        unittest.main()

    def test_convertar_para_json(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        expected_json = '[{"col1":1,"col2":3},{"col1":2,"col2":4}]'

        result = converter_para_json(df)

        # Assert that the JSON output is as expected
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()