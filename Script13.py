# AWS Security Audit Script 

import boto3
import logging


logging.basicConfig(
    filename="security_audit.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


iam = boto3.client("iam")
s3 = boto3.client("s3")
ec2 = boto3.client("ec2", region_name="ap-south-1")


try:
    
  iam_response = iam.list_users()

  for user in iam_response["Users"]:

    print(
      "User:",
      user["UserName"],
      "| Created:",
      user["CreateDate"]
    )

  logging.info("IAM users checked")


  s3_response = s3.list_buckets()

  for bucket in s3_response["Buckets"]:

    print(
      "Bucket:",
      bucket["Name"],
      "| Created:",
      bucket["CreationDate"]
    )

  logging.info("S3 buckets checked")


  ec2_response = ec2.describe_instances()

  public_count = 0

  for reservation in ec2_response["Reservations"]:

    for instance in reservation["Instances"]:

      if "PublicIpAddress" in instance:

        print(
          "Public EC2 Found:",
          instance["InstanceId"],
          "| Public IP:",
          instance["PublicIpAddress"]
        )

        logging.warning(
          f"Public EC2 detected {instance['InstanceId']}"
        )

        public_count += 1


  if public_count == 0:

      print("No public EC2 instances found")

      logging.info("No public EC2 instances found")

  logging.info("Security audit completed")


except Exception as e:

    print(e)

    logging.error(e)