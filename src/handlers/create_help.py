from src.entities.Address import Address
from src.entities.Helper import Helper
from src.entities.Help import Help
from src.errors.InvalidRequestBodyError import InvalidRequestBodyError
from src.providers.AWS import AWS
from src.providers.IdGenerator import IdGenerator
from src.repositories.DynamoDBHelpsRepository import DynamoDBHelpsRepository
from datetime import datetime
import json


def run(event, lambda_context=None):
    repository = DynamoDBHelpsRepository(AWS())

    body = json.loads(event['body'])
    
    try:
        helper_name = body.get('helper_name')
        helper_email = body.get('helper_email')
        helper_telephone = body.get('helper_telephone')
        street = body.get('street')
        neighborhood = body.get('neighborhood')
        house_number = body.get('house_number')
        complement = body.get('complement')
        description = body.get('description')

        if (
            not helper_name or
            not helper_email or
            not helper_telephone or
            not street or
            not neighborhood or
            not house_number or
            not description
        ):
            raise InvalidRequestBodyError('Body inválido')
        

        help_id = IdGenerator.generate()
        address_id = IdGenerator.generate()

        help_created_at = str(datetime.now())

        address = Address(
            address_id,
            street,
            neighborhood,
            house_number,
            complement
        )

        helper = Helper(
            helper_name,
            helper_email,
            helper_telephone
        )

        new_help = Help(
            help_id,
            address,
            helper,
            description,
            '',
            False,
            help_created_at
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