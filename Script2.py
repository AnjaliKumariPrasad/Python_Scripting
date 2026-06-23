import requests
import logging
import csv
import time
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "--url",
    required=True,
    help="Enter website URL"
)
args = parser.parse_args()
url = args.url


logging.basicConfig(
    filename="website.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def save_csv(current_time, url, status_code, response_time, status):

    with open("website_report.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            url,
            status_code,
            response_time,
            status
        ])



def check_website():

    while True:

        try:

            response = requests.get(url, timeout=5)

            status_code = response.status_code

            response_time = response.elapsed.total_seconds()

            current_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )


            if status_code == 200:

                if response_time > 2:
                    status = "SLOW"

                else:
                    status = "UP"

            else:
                status = "DOWN"


        except requests.exceptions.RequestException:

            current_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            status_code = "ERROR"

            response_time = "N/A"

            status = "DOWN"


        print("\n===== WEBSITE MONITOR =====")
        print("Time:", current_time)
        print("URL:", url)
        print("Status Code:", status_code)
        print("Response Time:", response_time)
        print("Website Status:", status)

        logging.info(
            f"URL:{url} "
            f"STATUS_CODE:{status_code} "
            f"RESPONSE_TIME:{response_time} "
            f"STATUS:{status}"
        )

        save_csv(
            current_time,
            url,
            status_code,
            response_time,
            status
        )

        time.sleep(10)


check_website()