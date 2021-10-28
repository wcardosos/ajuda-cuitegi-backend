import boto3


class AWS:
    @staticmethod
    def dynamo_db():
        return boto3.client('dynamodb')
    
    @staticmethod
    def sqs():
        return boto3.client('sqs')
    
    @staticmethod
    def s3():
        return boto3.client('s3')