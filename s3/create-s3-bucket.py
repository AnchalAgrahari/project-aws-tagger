import boto3
def create_s3_bucket(bucket_name):
    try:
        client = boto3.client('s3')
        response = client.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint':'us-west-2',
            },)
    except Exception as e:
        print("Exception occured", e)


if __name__ == '__main__':
    try:
        bucket_name=input("Enter the uniqe bucket name:").strip()
        if len(bucket_name) != 0:
            create_s3_bucket(bucket_name)
        else:
            print("Please enter the uniqe bucket name")
    except Exception as e:
        print("Exception occured",e)

    