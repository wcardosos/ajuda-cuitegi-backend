from unittest import TestCase, main
from unittest.mock import Mock, patch
from src.handlers.create_help import run as handler
import json


class TestCreateHelps(TestCase):
    def setUp(self) -> None:
        self.event_mock = {
            'body': {
                'person_to_help_name': 'Nome Pessoa Ajudada',
                'helper_name': 'Nome Pessoa Ajudante',
                'description': 'Descrição da ajuda',
                'contact': 'contato'
            }
        }

    @patch('src.handlers.create_help.AWS')
    def test_handler_create_help_correctly(self, aws_mock) -> None:
        with patch('src.handlers.create_help.IdGenerator.generate') as id_generator_spy:
            with patch('src.handlers.create_help.DynamoDBHelpsRepository.save') as dynamo_repository_spy:
                dynamo_repository_spy.save = Mock()
                result = handler(self.event_mock)

                id_generator_spy.assert_called_once()
                dynamo_repository_spy.assert_called_once()
                self.assertEqual(result['statusCode'], 201)

    @patch('src.handlers.create_help.AWS')
    def test_handler_returns_error_when_a_data_is_not_passed(self, aws_mock) -> None:
        event = self.event_mock
        del event['body']['description']

        with patch('src.handlers.create_help.IdGenerator.generate') as id_generator_spy:
            with patch('src.handlers.create_help.DynamoDBHelpsRepository.save') as dynamo_repository_spy:
                result = handler(event)

                id_generator_spy.assert_not_called()
                dynamo_repository_spy.assert_not_called()
                self.assertEqual(json.loads(result['body'])['message'], 'Body inválido')
                self.assertEqual(result['statusCode'], 400)
    


if __name__ == '__main__':
    main()