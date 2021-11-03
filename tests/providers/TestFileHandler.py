from unittest import TestCase, main
from unittest.mock import patch
from src.providers.FileHandler import FileHandler


class TestFileHandler(TestCase):
    def setUp(self) -> None:
        self.file_handler = FileHandler()

    @patch('src.providers.FileHandler.shutil.copy')
    def test_copy_correctly(self, shutil_copy_spy) -> None:
        MOCK_FILE = 'file'
        MOCK_FOLDER = 'folder'

        self.file_handler.copy(MOCK_FILE, MOCK_FOLDER)

        shutil_copy_spy.assert_called_once_with(MOCK_FILE, MOCK_FOLDER)
    
    @patch('src.providers.FileHandler.shutil.move')
    def test_move_correctly(self, shutil_move_spy) -> None:
        MOCK_FILE = 'file'
        MOCK_FOLDER = 'folder'

        self.file_handler.move(MOCK_FILE, MOCK_FOLDER)

        shutil_move_spy.assert_called_once_with(MOCK_FILE, MOCK_FOLDER)
    
    @patch('src.providers.FileHandler.shutil.make_archive')
    def test_zip_folder_correctly(self, make_archive_spy) -> None:
        MOCK_ZIP_FILE = 'file'
        MOCK_SOURCE_FOLDER = 'src'
        MOCK_DESTINATION_FOLDER = 'destination'
        ZIP_FILE_NAME = 'file.zip'

        with patch('src.providers.FileHandler.FileHandler.move') as file_handler_move_spy:
            self.file_handler.zip_folder(MOCK_ZIP_FILE, MOCK_SOURCE_FOLDER, MOCK_DESTINATION_FOLDER)

            make_archive_spy.assert_called_once_with(MOCK_ZIP_FILE, 'zip', MOCK_SOURCE_FOLDER)
            file_handler_move_spy.assert_called_once_with(ZIP_FILE_NAME, MOCK_DESTINATION_FOLDER)


if __name__ == '__main__':
    main()