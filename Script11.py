# EC2 Auto Tagging Script

import boto3

ec2 = boto3.client("ec2")

try:

  instance1 = ec2.describe_instances()

  for reservation in instance1["Reservations"]:
      
    for instance in reservation["Instances"]:

      if "Tags" not in instance:

        ec2.create_tags(
          Resources=[
            instance["InstanceId"]
          ],

          Tags=[
          {
            "Key": "Environment",
            "Value": "Dev"
          }
          ]
        )

        print(
            "Tagged",
            instance["InstanceId"]
        )


except Exception as e:

    print(e)