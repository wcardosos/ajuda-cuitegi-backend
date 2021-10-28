from unittest import TestCase, main
from unittest.mock import patch
from src.providers.AWS import AWS


class TestAWS(TestCase):
    @patch('src.providers.AWS.boto3.client')
    def test_dynamodb(self, boto3_client_spy):
        AWS.dynamo_db()

        boto3_client_spy.assert_called_once_with('dynamodb')

    @patch('src.providers.AWS.boto3.client')
    def test_sqs(self, boto3_client_spy):
        AWS.sqs()

        boto3_client_spy.assert_called_once_with('sqs')
    
    @patch('src.providers.AWS.boto3.client')
    def test_s3(self, boto3_client_spy):
        AWS.s3()

        boto3_client_spy.assert_called_once_with('s3')
    
if __name__ == '__main__':
    main()