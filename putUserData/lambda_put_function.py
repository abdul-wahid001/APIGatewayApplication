import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    print(table.item_count)
    status_code = 0
    response_body = ""
    user = json.loads(event['body'])
    print(type(user))
    print(user)
    try:
        response_body = table.put_item(
            Item={
                'id': user['id'],
                'firstname': user['firstname'],
                'last name': user['lastname']
            }
        )
        print(response_body)
        status_code = 200

    except :
        response_body = "Unable to put data due to some error please refer to logs"
        status_code = 403

    print(response_body)
    return {
        'statusCode': status_code,
        'headers': {
            "myHeader": "test"
        },
        'body': json.dumps(response_body)
    }
