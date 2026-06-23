# YAML/JSON Config Reader + Deployment Validator

import argparse
import json
from datetime import datetime
import csv
import logging


parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    required=True,
    help="enter file name"
)

args = parser.parse_args()

file = args.file


logging.basicConfig(
    filename="config.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def save_csv(current_time, file, status):

    with open(
        "config_report.csv",
        "a",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            current_time,
            file,
            status
        ])


def script():

    with open(file, "r") as file:

        data = json.load(file)


    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    if (
        "service" in data
        and
        "port" in data
        and
        "environment" in data
    ):

        status = "VALID"

    else:

        status = "INVALID"


    print("File:", file)

    print("Status:", status)


    save_csv(
        current_time,
        file,
        status
    )


    logging.info(
        f"FILE:{file} "
        f"STATUS:{status}"
    )


script()