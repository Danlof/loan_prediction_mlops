## Getting started with AWS
  #### Creating S3 bucket using CLI
```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

#### Create S3 bucket
`aws s3api create-bucket --bucket awsml-$RANDOM_ID`
- Upload file to the currently created bucket: `aws s3 cp Port.jpeg s3://awsml-bg5qxa` or `aws s3 cp Port.jpeg s3://awsml-$RANDOM_ID`
- Display storage class : `aws s3api list-objects-v2 --bucket awsml-bg5qxa` or `aws s3api list-objects-v2 --bucket awsml-$RANDOM_ID`

#### Clean up
Delete the file copied to your s3 bucket:`aws s3 rm s3://awsml-$RANDOM_ID/Port.jpeg` or `aws s3 rm s3://awsml-bg5qxa/Port.jpeg`

- Delete the s3 bucket: `aws s3api delete-bucket --bucket awsml-$RANDOM_ID` or `aws s3api delete-bucket --bucket awsml-bg5qxa`