from src.entities.Help import Help
from src.providers.AWS import AWS
import os

TABLE_NAME = os.getenv('HELP_TABLENAME')

class DynamoDBHelpsRepository:
    def __init__(self, aws: AWS) -> None:
        self.db = aws.dynamo_db()
        self.table = self.db.Table(TABLE_NAME)
    
    @classmethod
    def help_mapper(self, help_dynamo_item: dict) -> Help:
        return Help(
            help_dynamo_item['id'],
            help_dynamo_item['person_to_help_name'],
            help_dynamo_item['helper_name'],
            help_dynamo_item['description'],
            help_dynamo_item['contact'],
            help_dynamo_item['image_url'],
            help_dynamo_item['active']
        )

    
    def save(self, help: Help) -> None:
        item = {
            'id': help.id,
            'address': {
                'address_id': help.address.id,
                'street': help.address.street,
                'neighborhood': help.address.neighborhood,
                'number': help.address.number,
                'complement': help.address.complement
            },
            'helper': {
                'name': help.helper.name,
                'email': help.helper.email,
                'telephone': help.helper.telephone
            },
            'description': help.description,
            'image_url': help.image_url,
            'active': help.active,
            'created_at': help.created_at,
            'updated_at': help.updated_at
        }

        self.table.put_item(Item=item)
    
    def get_all(self):
        items = self.table.scan()['Items']

        all_helps = map(self.help_mapper, items)

        return all_helps