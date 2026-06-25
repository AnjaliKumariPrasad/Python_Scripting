import boto3
import logging

lambda_client = boto3.client("lambda")
ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

try:

    print("\nEC2 INSTANCES")

    response1 = ec2.describe_instances()

    for reservation in response1["Reservations"]:

        for instance in reservation["Instances"]:

            print(
                instance["InstanceId"],
                instance["State"]["Name"],
                instance["InstanceType"]
            )

    print("\nS3 BUCKETS")

    response2 = s3.list_buckets()

    for bucket in response2["Buckets"]:

        print(bucket["Name"])


    print("\nLAMBDA FUNCTIONS")

    response3 = lambda_client.list_functions()

    for function in response3["Functions"]:

        print(function["FunctionName"])



except Exception as e:

    print(e)

