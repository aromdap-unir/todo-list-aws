import json
import os
from todolist import App
# from dummy_todolist import App
# import requests


def handler(event, context):
    from pythonping import ping

    ping('dynamodb_endpoint', verbose=True)
    # raise Exception('eerrorrr')
    app = App()
    print(event)
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
            "body": json.dumps({
                "message": "Error: Endpoint not found!",
                # "location": ip.text.replace("\n", "")
            }),
        }
