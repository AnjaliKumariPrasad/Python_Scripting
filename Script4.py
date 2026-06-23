#Disk Cleanup Automation Script

import argparse
import os
import logging


parser = argparse.ArgumentParser()

parser.add_argument(
    "--path",
    required=True,
    help="Enter folder path"
)
args = parser.parse_args()
path = args.path

logging.basicConfig(
    filename="cleanup.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)


def cleanup():
    files = os.listdir(path)

    deleted_count = 0

    deleted_files = []


    for file in files:

        if file.endswith(".log"):

            file_path = os.path.join(
                path,
                file
            )

            os.remove(file_path)

            deleted_count += 1

            deleted_files.append(file)


    print("\n===== REPORT =====")
    print("deleted files:", deleted_count)

    with open(
        "deleted.txt",
        "w"
    ) as f:

        for item in deleted_files:

            f.write(item + "\n")


    logging.info(
        f"path:{path} "
        f"delete:{deleted_count}"
    )


cleanup()