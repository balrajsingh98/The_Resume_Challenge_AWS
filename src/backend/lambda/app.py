pipimport json
import boto3
from boto3.dynamodb.conditions import Key 

TABLE_NAME = "visitor-table"  
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# create the DynamoDB Table Resource
dynamodb_table = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb_table.Table(TABLE_NAME)

def lambda_handler(event, context):
    response = table.get_item(
        TableName =TABLE_NAME,
        Key={
            "record_id":'VisitorCount',
        }
        )
    item = response['Item']

    table.update_item(
        Key={
            "record_id":'VisitorCount',
        },
        UpdateExpression='SET visitor_count = :val1',
        ExpressionAttributeValues={
            ':val1': item['visitor_count'] + 1
        }
    )
    return{
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
      "body": json.dumps({"Visit_Count": str(item['visitor_count'] + 1)})
    }
