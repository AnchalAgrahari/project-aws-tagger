import boto3
import json
def add_tag(bucket_name):
    try:
        client = boto3.client('s3')
        response = client.put_bucket_tagging(
        Bucket= bucket_name,
        ChecksumAlgorithm='CRC32',
        Tagging={
            'TagSet': [
                {
                    'Key': 'owner',
                    'Value': 'Anchal'
                },
            ]
        },
        ExpectedBucketOwner='697429983773'
    )
        
    except Exception as e:
        print("Exception occured", e)

def lambda_handler(event, context):
    # TODO implement
    try:
        bucket_name = "project-aws-tagger-lambda-22-04-2025"
        if len(bucket_name) != 0:
            add_tag(bucket_name)
        else:
            print("Please Enter the unique bucket name !")
    except Exception as e:
        print("Exception Occured!",e)
