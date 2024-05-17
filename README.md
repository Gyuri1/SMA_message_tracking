# SMA_message_tracking

This python script demonstrates how to use  Message Tracking API capabilities of Security Management Appliance (SMA)

# How to install

Please download all files and install requests python module:

`pip install requests`


# How to use

There are a 2 parameters:
 -d  : number of days (mandatory)
 -m  : message ID (optional)


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
