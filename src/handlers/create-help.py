from entities.Help import Help
from providers.AWS import AWS
from providers.IdGenerator import IdGenerator
from repositories.DynamoDBHelpsRepository import DynamoDBHelpsRepository


def run(event):
    repository = DynamoDBHelpsRepository(AWS())
    
    try:
        person_to_help_name = event['body']['person_to_help_name']
        helper_name = event['body']['helper_name']
        description = event['body']['description']
        contact = event['body']['contact']

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
            'statusCode': 200
        }
    except Exception as error:
        return {
            'body': {
                'error': error
            },
            'statusCode': 400
        }