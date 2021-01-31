import json
import logging
import os
import time
import uuid

import boto3

import decimal
import decimalencoder

class App():
    def __init__(self):
        print(os.environ)
        if os.getenv('STAGE') == 'test':
            print('>> DynamoDB: Starting creation of testing instance')
            self.dynamodb = boto3.resource('dynamodb', 
                                            endpoint_url='http://dynamodb:8000')
        else:
            print('>> DynamoDB: Starting creation of production instance')
            self.dynamodb = boto3.resource('dynamodb')

        #self.table = self._create_table(os.getenv('STAGE'))
        
    def _create_table(self, tablename_):
        table = self.dynamodb.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            TableName=tablename_,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='todoTable')
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()

        return self.dynamodb.Table(os.getenv('DYNAMODB_TABLE'))

    def try_me(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('pang')
        }
    
        return response

    def create(self, event, context):
        logging.info('You have accessed the __create__ endpoint!')
        data = json.loads(event['body'])
        if 'text' not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't create the todo item.")
        
        timestamp = str(time.time())
    
        item = {
            'id': str(uuid.uuid1()),
            'text': data['text'],
            'checked': False,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }
    
        # write the todo to the database
        self.table.put_item(Item=item)
    
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }
    
        return response
    
    def delete(self, event, context):
        logging.info('You have accessed the __delete__ endpoint!')   
        # delete the todo from the database
        self.table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
        deleted = f"Deleted ID: {event['pathParameters']['id']}"        
        
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(deleted)
        }
    
        return response
        
    def get(self, event, context):
        logging.info('You have accessed the __get__ endpoint!') 
        # fetch todo from the database
        result = self.table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
    
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Item'],
                               cls=decimalencoder.DecimalEncoder)
        }

        return response
    
    def show(self, event, context):
        logging.info('You have accessed the __show__ endpoint!') 
        table = self.dynamodb.Table(os.getenv('DYNAMODB_TABLE'))

        result = table.scan()
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
        }
    
        return response
        
    def translate(self, event, context):
        logging.info('You have accessed the __translate__ endpoint!') 
        # fetch todo from the database
        result = self.table.get_item(
            Key={
                'id': event['pathParameters']['id'],
            }
        )
    
        try:
            item = result['Item']
    
            # comprehend origin language
            comprehend = boto3.client(service_name='comprehend',
                                      region_name='us-east-1')
            related = comprehend.detect_dominant_language(Text=item['text'])
    
            # translate result text
            translate = boto3.client(service_name='translate',
                                     region_name='us-east-1',
                                     use_ssl=True)
    
            translation = translate.translate_text(
                Text=item['text'],
                SourceLanguageCode=related['Languages'][0]['LanguageCode'],
                TargetLanguageCode=event['pathParameters']['lang'])
    
            item['text'] = translation['TranslatedText']
    
            # create a response
            response = {
                "statusCode": 200,
                "body": json.dumps(item,
                                   cls=decimalencoder.DecimalEncoder)
            }
    
            return response
    
        except Exception as e:
            logging.error(str(e))
            raise Exception("[ErrorMessage]: " + str(e))
            
    def update(self, event, context):
        logging.info('You have accessed the __update__ endpoint!') 
        data = json.loads(event['body'])
        if 'text' not in data or 'checked' not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't update the todo item.")
    
        timestamp = int(time.time() * 1000)

        # update the todo in the database
        result = self.table.update_item(
            Key={
                'id': event['pathParameters']['id']
            },
            ExpressionAttributeNames={
              '#todo_text': 'text',
            },
            ExpressionAttributeValues={
              ':text': data['text'],
              ':checked': data['checked'],
              ':updatedAt': timestamp,
            },
            UpdateExpression='SET #todo_text = :text, '
                             'checked = :checked, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW',
        )
    
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Attributes'],
                               cls=decimalencoder.DecimalEncoder)
        }
    
        return response