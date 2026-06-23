#Log File Analyzer Script

import argparse
import logging
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file",
    required=True,
    help="Enter log file name"
)
args = parser.parse_args()
file_name = args.file


logging.basicConfig(
    filename="analyzer.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def save_csv(current_time, total_logs, error_count, warning_count, info_count):

    with open(
        "log_report.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            total_logs,
            error_count,
            warning_count,
            info_count
        ])


def analyze():

    try:

        error_count = 0
        warning_count = 0
        info_count = 0
        total_logs = 0

        with open(file_name, "r") as file:

            for line in file:

                total_logs += 1

                if "ERROR" in line:

                    error_count += 1

                elif "WARNING" in line:

                    warning_count += 1

                elif "INFO" in line:

                    info_count += 1

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


  
        print("\n===== LOG REPORT =====")
        print("file:", file_name)
        print("total logs:", total_logs)
        print("error count:", error_count)
        print("warning count:", warning_count)
        print("info count:", info_count)

        save_csv(
            current_time,
            total_logs,
            error_count,
            warning_count,
            info_count
        )

        logging.info(
            f"FILE:{file_name} "
            f"TOTAL:{total_logs} "
            f"ERROR:{error_count} "
            f"WARNING:{warning_count} "
            f"INFO:{info_count}"
        )


    except FileNotFoundError:

        print("File not found")

        logging.error(
            "Log file not found"
        )

analyze()