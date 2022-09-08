import datetime
import time

utc = "2020-12-15T09:14:13.916984565Z".split(".")[0]
UTC_FORMAT = "%Y-%m-%dT%H:%M:%S"
utc_time = datetime.datetime.strptime(utc, UTC_FORMAT)
local_time = utc_time + datetime.timedelta(hours=8)
print(local_time)