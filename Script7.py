# Linux Command Runner + System Troubleshooter

import subprocess
import argparse
import logging
import csv
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument(
    "--command",
    required=True,
    help="Type Linux command"
)
args = parser.parse_args()
command = args.command

logging.basicConfig(
    filename="command.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def save_csv(current_time, command, status):

    with open(
        "command_report.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            command,
            status
        ])

def linux():

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        # check success
        if result.returncode == 0:

            status = "SUCCESS"

        else:

            status = "FAILED"


        print("\n===== COMMAND REPORT =====")
        print("Command:", command)
        print("Status:", status)
        print("\nOutput:")
        print(result.stdout)


        # save output file
        with open(
            "command_output.txt",
            "w"
        ) as file:

            file.write(
                result.stdout
            )


        # save csv
        save_csv(
            current_time,
            command,
            status
        )


        # logging
        logging.info(
            f"COMMAND:{command} "
            f"STATUS:{status}"
        )


    except Exception as e:

        print("Error:", e)

        logging.error(
            f"COMMAND FAILED {command}"
        )


linux()