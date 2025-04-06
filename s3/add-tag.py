import boto3
def add_tag(tag_name):
    try:
        client = boto3.client('s3')
        response = client.put_bucket_tagging(
        Bucket='tag-implementation-on-05-04-2025',
        ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256'|'CRC64NVME',
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
        add_tag(tag_name)
    except Exception as e:
        print("An Exception Occured !!",e)