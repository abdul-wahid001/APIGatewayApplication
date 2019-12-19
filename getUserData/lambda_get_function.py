import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    print(table.item_count)
    status_code = 0
    repsonse_body= ""
    print(event)
    id = event['pathParameters']['id']
    print(id)
    try:
        response_body = table.get_item(
            Key={
                'id': id
            }
        )
        response_body=response_body['Item']
        print(response_body)
        status_code = 200
    except:
        response_body = "Unable to retrieve data due to some error please refer to logs"
        status_code = 403

    print(response_body)
    return {
        'statusCode': status_code,
        'headers': {
            "myHeader": "test"
        },
        'body': json.dumps(response_body)
    }
