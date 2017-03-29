1. Converting unix timestamp string to readable date in Python

dat = "1490918400"

import datetime

print(
    datetime.datetime.fromtimestamp(
        int("1490918400")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

2017-03-31 05:30:00

2. 13 digit unix time convert in python
 
import time
timestamp = 1487924069089
time.strftime("%a %d %b %Y %H:%M:%S GMT", time.gmtime(timestamp / 1000.0))

time.strftime("%a %d %b %Y", time.gmtime(timestamp / 1000.0))

Fri 24 Feb 2017 
st = time.strftime("%d-%b-%Y %a %H:%M:%S GMT", time.gmtime(timestamp / 1000.0))
