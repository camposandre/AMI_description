import csv
import boto3

#call your s3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('acr-ec2-description')
key = 'AMIdescription.csv'

ec2 = boto3.client('ec2')

# creates the csv file
with open('AMIdescription.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # creates the header
    header = ['OwnerID', 'ImageID', 'Name', 'State', 'Image_Location', 'Public', 'Description']

    # write the header
    writer.writerow(header)


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

    # collect the data for writing to csv file
    for ami in response:
        print('==========PROCESSANDO===========')

        #write the data
        data = [response['Images'][0]['OwnerId'], response['Images'][0]['ImageId'], response['Images'][0]['Name'], response['Images'][0]['State'], response['Images'][0]['ImageLocation'], response['Images'][0]['Public'], response['Images'][0]['Description']]


        # write the data to csv file
        writer.writerow(data)

#upload the data into s3
bucket.upload_file('AMIdescription.csv', key)
