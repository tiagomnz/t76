#!/bin/python

from _datetime import datetime
hour_now=datetime.toordinal(datetime.now())
hour_initial=0
h =  hour_now - hour_initial
hour = datetime.now().strftime('%H:%M')
print (h)