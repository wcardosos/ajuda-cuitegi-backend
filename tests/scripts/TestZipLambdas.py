from unittest import TestCase, main
from unittest.mock import patch
from src.scripts.zip_lambdas import get_path_file, get_import_strings, verify_custom_import
from tests.mocks.stubs.FileStub import FileStub


class TestZipLambdas(TestCase):
    def test_get_filename_correctly(self) -> None:
        MOCK_IMPORT_STR = 'from src.package.Class import Class'
        EXPECTED_FILE_PATH = 'src/package/Class/Class.py'

        result = get_path_file(MOCK_IMPORT_STR)

        self.assertEqual(result, EXPECTED_FILE_PATH)
    
    def test_verify_custom_import_correctly(self) -> None:
        MOCK_LINE = 'from src.packages.Class import Class'

        result = verify_custom_import(MOCK_LINE)

        self.assertTrue(result)

    def test_verify_custom_import_returns_false_when_not_line_of_import(self) -> None:
        MOCK_LINE = 'n = 1'

        result = verify_custom_import(MOCK_LINE)

        self.assertFalse(result)
    
    @patch('src.scripts.zip_lambdas.open', return_value=FileStub())
    def test_get_import_strings(self, file_stub) -> None:
        EXPECTED_IMPORT_STRINGS = [
            'from src.packages.Class import Class',
            'from src.packages.OtherClass import OtherClass'
        ]

        result = get_import_strings('path')

        self.assertEqual(result, EXPECTED_IMPORT_STRINGS)

if __name__ == '__main__':
    main()