# Stop All Running EC2 Instances

import boto3
import logging


logging.basicConfig(
    filename="command.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

ec2 = boto3.client("ec2")

try:

  instance1 = ec2.describe_instances()

  for reservation in instance1["Reservations"]:

    for instance in reservation["Instances"]:

      if instance["State"]["Name"] == "running":

        ec2.stop_instances(
          InstanceIds=[
            instance["InstanceId"]
          ]
        )

        print(
          "Stopped",
          instance["InstanceId"]
        )


        logging.info(
          f"Stopped {instance['InstanceId']}"
        )

except Exception as e:

    print(e)

    logging.error(e)