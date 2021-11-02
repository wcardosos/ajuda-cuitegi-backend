from src.entities.Help import Help
from src.errors.InvalidRequestBodyError import InvalidRequestBodyError
from src.providers.AWS import AWS
from src.providers.IdGenerator import IdGenerator
from src.repositories.DynamoDBHelpsRepository import DynamoDBHelpsRepository
import json


def run(event, lambda_context=None):
    repository = DynamoDBHelpsRepository(AWS())

    body = json.loads(event['body'])
    
    try:
        person_to_help_name = body.get('person_to_help_name')
        helper_name = body.get('helper_name')
        description = body.get('description')
        contact = body.get('contact')

        if not person_to_help_name or not helper_name or not description or not contact:
            raise InvalidRequestBodyError('Body inválido')
        

        help_id = IdGenerator.generate()

        new_help = Help(
            help_id,
            person_to_help_name,
            helper_name,
            description,
            contact,
            '',
            False
        )

        repository.save(new_help)

        return {
            'headers': {
                'Content-Type': 'application/json'
            },
            'statusCode': 201
        }
    except Exception as error:
        return {
            'body': json.dumps({
                'message': str(error)
            }),
            'headers': {
                'Content-Type': 'application/json'
            },
            'statusCode': 400
        }