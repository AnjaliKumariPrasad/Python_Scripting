# Server Resource Alert System

import logging
import psutil
import csv
import time
from datetime import datetime


logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def save_csv(current_time, cpu, ram, disk, status):

    with open(
        "server_report.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            cpu,
            ram,
            disk,
            status
        ])


def server():

    while True:

        cpu = psutil.cpu_percent(1)

        ram = psutil.virtual_memory().percent

        disk = psutil.disk_usage("/").percent


        if cpu > 80 or ram > 80 or disk > 90:

            status = "WARNING"

        else:

            status = "GOOD"


        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        print("\n===== SERVER REPORT =====")

        print("CPU:", cpu)

        print("RAM:", ram)

        print("DISK:", disk)

        print("STATUS:", status)


        save_csv(
            current_time,
            cpu,
            ram,
            disk,
            status
        )


        logging.info(
            f"CPU:{cpu} "
            f"RAM:{ram} "
            f"DISK:{disk} "
            f"STATUS:{status}"
        )


        time.sleep(10)


server()