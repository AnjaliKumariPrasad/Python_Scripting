# Service Health Checker Script

import argparse
import logging
import psutil


parser = argparse.ArgumentParser()
parser.add_argument(
    "--services",
    required=True,
    help="Enter services separated by comma"
)
args = parser.parse_args()
services = args.services.split(",")


logging.basicConfig(
    filename="service.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)


def checker():

    healthy = 0
    failed = 0

    for service in services:

        found = False

        for process in psutil.process_iter():

            try:

                if process.name().lower() == service.lower():

                    print(service, ": RUNNING")

                    healthy += 1

                    found = True

                    break

            except:

                pass


        if found == False:

            print(service, ": NOT RUNNING")

            failed += 1


    print("\nHealthy Services:", healthy)
    print("Failed Services:", failed)

    logging.info(
        f"healthy:{healthy} failed:{failed}"
    )

checker()