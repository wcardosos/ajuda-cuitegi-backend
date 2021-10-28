import boto3

REGION = boto3.Session().region_name

class AWS:
    @staticmethod
    def dynamo_db():
        return boto3.resource('dynamodb', REGION)
    
    @staticmethod
    def sqs():
        return boto3.client('sqs')
    
    @staticmethod
    def s3():
        return boto3.client('s3')