import json
import logging
import os
import time
import uuid
import boto3
import decimal
import json
import decimalencoder


class App():
    def __init__(self):
        """docstring for __init__"""
        # TODO: write code...
        self.dynamodb = boto3.resource('dynamodb')
        
        
    def create(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __create__ endpoint!')
        }
        return response

    def delete(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __delete__ endpoint!')
        }
        return response

    def get(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __get__ endpoint!')
        }
        return response
    
    def show(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __show__ endpoint!')
        }
        return response
        
    def translate(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __translate__ endpoint!')
        }
        return response
    
            
    def update(self, event, context):
        response = {
            "statusCode": 200,
            "body": json.dumps('You have accessed the __update__ endpoint!')
        }
        return response