import argparse
import shutil
import logging
import os
import csv
from datetime import datetime


# ---------- ARGUMENT ----------

parser = argparse.ArgumentParser()
parser.add_argument(
    "--path",
    required=True,
    help="Enter folder path"
)
args = parser.parse_args()
path = args.path


logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def save_csv(current_time, backup_file, size):

    with open(
        "backup_report.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            backup_file,
            size
        ])


def backup():

    current_time = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    backup_file = shutil.make_archive(
        f"backup_{current_time}",
        "zip",
        path
    )

    size = os.path.getsize(
        backup_file
    )

    size_mb = round(
        size / (1024 * 1024),
        2
    )

    print("\n===== BACKUP REPORT =====")
    print("Path:", path)
    print("Backup File:", backup_file)
    print("Backup Size:", size_mb, "MB")

    save_csv(
        current_time,
        backup_file,
        size_mb
    )

    logging.info(
        f"path:{path} "
        f"file:{backup_file} "
        f"size:{size_mb}MB"
    )

backup()