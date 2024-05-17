# SMA_message_tracking

This python script demonstrates how to use  Message Tracking API capabilities of Security Management Appliance (SMA)

# How to install:  

Please download all the files from this repository and install `requests` python module:
`pip install requests`

Modify the `sma_credentials.py` file content according to Your parameters!

# How to use:  

There are a 2 parameters:  
 -d  : number of days (mandatory)  
 -m  : message ID (optional)  
     

The script will list all of the messages if You do not specify the Message ID.  


Example:

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
