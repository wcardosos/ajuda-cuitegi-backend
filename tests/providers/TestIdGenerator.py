from unittest import TestCase, main
from unittest.mock import patch
from src.providers.IdGenerator import IdGenerator


class TestAWS(TestCase):
    @patch('src.providers.IdGenerator.uuid4', return_value='id')
    def test_generate(self, generate_stub) -> None:
        EXPECTED_ID = 'id'
        
        id = IdGenerator.generate()

        self.assertEqual(id, EXPECTED_ID)

if __name__ == '__main__':
    main()