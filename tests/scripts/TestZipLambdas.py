from unittest import TestCase, main
from src.scripts.zip_lambdas import get_path_file


class TestZipLambdas(TestCase):
    def test_get_filename_correctly(self) -> None:
        IMPORT_STR = 'from src.package.Class import Class'
        EXPECTED_FILE_PATH = 'src/package/Class/Class.py'

        result = get_path_file(IMPORT_STR)

        self.assertEqual(result, EXPECTED_FILE_PATH)

if __name__ == '__main__':
    main()