import os
import json
import requests


def handler(event, context):

    url = os.environ['webhook_url']
    payload = {"text": "これは、チャンネル内のテキスト行です。\nそしてもう1つテキスト行があります。"}
    r = requests.post(
        url,
        data=json.dumps(payload)
    )
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit'
    }
