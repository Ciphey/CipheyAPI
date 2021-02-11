import json
from ciphey import decrypt
from ciphey.iface import Config

def lambda_handler(event, context):
    to_find = json.loads(event["body"])

    ctext = to_find["ctext"].strip()

    res = decrypt(
        Config().library_default().complete_config(),
        ctext,
    )
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
