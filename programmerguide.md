# Follow the following Instructions for S3 Setup:
### Step 1: Clone the project
### Step 2: You need to setup following AWS Credentials in Settings.py. Note, You must have a AWS account. 
```
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = 'bucketName'
AWS_DEFAULT_ACL = None
AWS_REGION = ''
```

### Step 3: Create Amazon S3 Bucket policy for your bucket.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket1",
                "arn:aws:s3:::bucket1/*"
            ]
        }
    ]
}
```

### Step 4: Run necessary migrations if needed. Then, run the server.