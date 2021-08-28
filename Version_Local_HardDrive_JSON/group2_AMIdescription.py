import json
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(
    Filters=[
        {
            'Name': 'is-public',
            'Values': [
                'false'
            ]
        }
    ]
)

print("===============PROCESSANDO================")

# creates the json file
with open('AMI_description.json', 'w', encoding='UTF8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)
