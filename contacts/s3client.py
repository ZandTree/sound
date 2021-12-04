import uuid
import io
import boto3
from django.conf import settings


S3_BASE_URL = 'https://s3.eu-central-1.amazonaws.com/'
BUCKET=settings.BUCKET_NAME

s3_client = boto3.client(
    's3',
    endpoint_url = S3_BASE_URL,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name='eu-central-1'
    )


def upload_img(bucket=BUCKET,acl='public-read'):
    end = uuid.uuid4().hex[:6] 
    path = 'foo-'+str(end)+'.jpg'    
    # print('path',path) foo-1f7537.jpg
    with open('lemon.jpg','rb') as fh:
        file = io.BytesIO(fh.read())
    try:
        s3_client.upload_fileobj(
            file,
            BUCKET,
            path,
            ExtraArgs={
                'ACL':acl
            }
        )
    except:
        print('error occurred  uploading file to s3')

# TODO: create model incl url field
# def upload_img_2(file_name):
#     s3_client = boto3.client('s3')
#     key = uuid.uuid4().hex[:6] + file_name
#     url = f'{S3_BASE_URL}{BUCKET}/{key}'
#     try:
#         s3_client.upload_fileobj(file_name,BUCKET,key)
#     except:
#         print('error occurred  uploading file to s3',url)