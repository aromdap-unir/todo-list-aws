import json
import os
from todolist import App

def handler(event, context):
    '''
    1. Get instance of the app class
    2. Generate enpoint looking at matches between path and the app method name
    3. Access the requested method dynamically passing the event as a parameter
    '''
    app = App()
    path = event['path'].split('/')[1]
    endpoints = {
        'create': app.create,
        'delete': app.delete,
        'get': app.get,
        'show': app.show,
        'translate': app.translate,
        'update': app.update,
        'try_me': app.try_me
    }
    if path in endpoints:
        return endpoints[path](event,context)
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Error: Endpoint not found!"}),
        }
