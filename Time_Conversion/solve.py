#!/bin/python
import sys
from datetime import datetime

def timeConversion(s):
    # Complete this function
    datetime_object = datetime.strptime(s, '%I:%M:%S%p')
    return datetime_object.strftime("%H:%M:%S")

s = raw_input().strip()
result = timeConversion(s)
print(result)


