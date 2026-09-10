import json
import boto3
import os

ses = boto3.client('ses', region_name='ap-south-1')

SENDER = os.environ['SENDER_EMAIL']
RECIPIENT = os.environ['RECIPIENT_EMAIL']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        name = body.get('name', 'Anonymous')
        email = body.get('email', 'No email provided')
        message = body.get('message')

        if not message:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing "message" in request body'})
            }

        email_body = f"New contact form submission\n\nFrom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': f'New contact form message from {name}'},
                'Body': {'Text': {'Data': email_body}}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Message sent successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }