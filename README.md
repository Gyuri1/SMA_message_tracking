# SMA_message_tracking

This Python script demonstrates how to leverage the Message Tracking API capabilities of Cisco's Security Management Appliance (SMA).  


# How to install:  

To get started, download all the files from this repository. Then, install the `requests` Python module by running:  

```bash
pip install requests
```  


Update the contents of the `sma_credentials.py` file with Your specific configuration parameters!  
  

# How to use:  

The script accepts two parameters:
	•	-d : The number of days to look back for messages (mandatory)
	•	-m : A specific message ID to track (optional)
     

By default, the script will list all messages within the specified date range if no message ID is provided.


Expected output:


To track messages from the last 1 day and filter by a specific message ID (e.g., 11244), use the following command:

```py
python3 sma_message_tracking.py  -d 1 -m 11244
Retrieving messages the SMA...
Messages retrieved: 35
Message MID: 11244  {
    "11243": [
        "user1@xxxxx.com"
    ],
    "11244": [
        "noreply@xxxxx.com"
    ]
}

```

# Useful reference:  
For more information about the Message Tracking API, refer to the Cisco ESA API Guide 15.0:
https://www.cisco.com/c/en/us/td/docs/security/esa/esa15-0/api_guide/b_Secure_Email_API_Guide_15-0/b_ESA_API_Guide_chapter_010.html#id_91367


