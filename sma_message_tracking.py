"""

This python script demonstrates how to use  Message Tracking API capabilities of Security Management Appliance (SMA)

"""

import argparse
import json
import time
import requests
from  sma_credentials import *

from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

# Disable certificate warnings (not recommended for production use)
requests.packages.urllib3.disable_warnings()

# System Parameters
port = "4431"


def get_message_tracking_data(start_date, end_date, offset: int = 0, limit: int = 20):
    """ Function for retrieving messages from the SMA """
    print("Retrieving messages the SMA...")
    
    total_responses = limit
    full_response = []
    while total_responses == limit:

        url = f"https://{sma_hostname}:{port}/sma/api/v2.0/message-tracking/messages?" \
              f"startDate={start_date}.000Z&endDate={end_date}.000Z&ciscoHost=All_Hosts&searchOption=messages" \
              f"&offset={offset}&limit={limit}"
        try:
            # retrieving messages from the SMA
            response = requests.get(url, auth=HTTPBasicAuth(sma_username, sma_password), verify=False)
            # Check bad responses
            if response.status_code >= 200 and response.status_code < 300:

                # Number of responses 
                total_responses = response.json()["meta"]["num_bad_records"] + response.json()["meta"]["totalCount"]

                # Update the full response
                for message in response.json()["data"]:
                    full_response.append(message)
            else:
                print(json.dumps(response.json(), indent=4))
                exit()

        except Exception as err:
            print("Error fetching info from SMA: " + str(err))
        # Increment the offset
        offset += limit

    return full_response


def main(mid, days):
    # Make a timestamp for a few days ago
    past = datetime.utcnow().replace(second=0, microsecond=0) - timedelta(days=int(days))
    # Convert into ISO Format
    start_date = past.isoformat()

    # Get the current timestamp in ISO Format
    end_date = datetime.utcnow().replace(second=0, microsecond=0).isoformat()

    # Get the last days' messages from the SMA
    message_data = get_message_tracking_data(start_date, end_date)

    print(f"Messages retrieved: {len(message_data)}")

    if mid:
        # Iterate through all messages
        for message in message_data:
            if "attributes" in message:
                if "mid" in message['attributes']:
                    if int(mid) in message['attributes']['mid']:
                        print(f"Message MID: {mid} ",json.dumps(message['attributes']['recipientMap'], indent=4))
    else:
        # Show all messages
        print(f"Messages:",json.dumps(message_data, indent=4))    
                        

# MAIN function 
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(
        description="This script shows how to track messages in SMA based on Message ID (MID)"
    )
    parser.add_argument("-m", help="message ID", required=False)
    parser.add_argument("-d", help="how many days back", required=True)
    
    args = parser.parse_args()

    main(args.m, args.d)
