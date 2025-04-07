import boto3
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
        print("Exception occured",e)

if __name__=='__main__':
    try:
        bucket_name=input("Enter the uniqe bucket name:").strip()
        if len(bucket_name) != 0:
            add_tag(bucket_name)
        else:
            print("Please enter the unique bucket name! ")
    except Exception as e:
        print("An Exception Occured !!",e)