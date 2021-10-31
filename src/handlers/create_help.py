from src.entities.Help import Help
from src.errors.InvalidRequestBodyError import InvalidRequestBodyError
from src.providers.AWS import AWS
from src.providers.IdGenerator import IdGenerator
from src.repositories.DynamoDBHelpsRepository import DynamoDBHelpsRepository


def run(event, lambda_context=None):
    repository = DynamoDBHelpsRepository(AWS())
    
    try:
        person_to_help_name = event.get('body').get('person_to_help_name')
        helper_name = event.get('body').get('helper_name')
        description = event.get('body').get('description')
        contact = event.get('body').get('contact')

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
            'statusCode': 201
        }
    except Exception as error:
        return {
            'body': {
                'message': str(error)
            },
            'statusCode': 400
        }