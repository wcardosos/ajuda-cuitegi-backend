from unittest import TestCase, main
from unittest.mock import patch
from src.scripts.zip_lambdas import (
    create_folder,
    create_project_folders,
    get_filename_from_import_string,
    get_import_strings,
    get_path_file,
    get_project_root_folder,
    get_up_folder,
    verify_custom_import,
    verify_folder_exists
)
from tests.mocks.stubs.FileStub import FileStub


class TestZipLambdas(TestCase):
    def test_verify_custom_import_correctly(self) -> None:
        MOCK_LINE = 'from src.packages.Class import Class'

        result = verify_custom_import(MOCK_LINE)

        self.assertTrue(result)
    
    def test_verify_custom_import_returns_false_when_not_line_of_import(self) -> None:
        MOCK_LINE = 'n = 1'

        result = verify_custom_import(MOCK_LINE)

        self.assertFalse(result)
    
    @patch('src.scripts.zip_lambdas.os.path.exists')
    def test_verify_folder_exists_when_exists(self, os_path_exists_spy) -> None:
        os_path_exists_spy.return_value = True

        result = verify_folder_exists('path')

        self.assertTrue(result)

    @patch('src.scripts.zip_lambdas.os.path.exists')
    def test_verify_folder_exists_when_not_exists(self, os_path_exists_stub) -> None:
        os_path_exists_stub.return_value = False

        result = verify_folder_exists('path')

        self.assertFalse(result)
    
    def test_get_filename_from_import_string_correctly(self) -> None:
        MOCK_IMPORT_STRING = 'path/filename'
        EXPECTED_FILENAME = 'filename'

        result = get_filename_from_import_string(MOCK_IMPORT_STRING)

        self.assertEqual(result, EXPECTED_FILENAME)
    
    @patch('src.scripts.zip_lambdas.open', return_value=FileStub())
    def test_get_import_strings(self, file_stub) -> None:
        EXPECTED_IMPORT_STRINGS = [
            'from src.packages.Class import Class',
            'from src.packages.OtherClass import OtherClass'
        ]

        result = get_import_strings('path')

        self.assertEqual(result, EXPECTED_IMPORT_STRINGS)

    def test_get_path_file_correctly(self) -> None:
        MOCK_IMPORT_STR = 'from src.package.Class import Class'
        EXPECTED_FILE_PATH = 'src/package/Class.py'

        result = get_path_file(MOCK_IMPORT_STR)

        self.assertEqual(result, EXPECTED_FILE_PATH)
    
    @patch('src.scripts.zip_lambdas.os.getcwd')
    def test_get_project_root_folder_correctly(self, os_getcwd_stub) -> None:
        MOCK_FOLDER = '/src/scripts/folder'
        EXPECTED_ROOT_FOLDER = '/folder'
        os_getcwd_stub.return_value = MOCK_FOLDER

        result = get_project_root_folder()

        self.assertEqual(result, EXPECTED_ROOT_FOLDER)
    
    def test_get_up_folder_correctly(self) -> None:
        MOCK_FILENAME = '/src/scripts/folder.py'
        EXPECTED_UP_FOLDER = '/src/scripts'

        result = get_up_folder(MOCK_FILENAME)

        self.assertEqual(result, EXPECTED_UP_FOLDER)
    
    @patch('src.scripts.zip_lambdas.os.mkdir')
    def test_create_folder_correctly(self, os_mkdir_spy) -> None:
        create_folder('path')

        os_mkdir_spy.assert_called_once()

    @patch('src.scripts.zip_lambdas.os.mkdir')
    def test_create_projects_folders(self, os_mkdir_spy) -> None:
        create_project_folders('path')

        self.assertEqual(os_mkdir_spy.call_count, 5)
    

if __name__ == '__main__':
    main()