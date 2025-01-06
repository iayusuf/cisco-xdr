from datetime import datetime, timedelta
import sys
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    # python version < 3.3
    import time
    def timestamp(date):
        return time.mktime(date.timetuple())
else:
    def timestamp(date):
        return date.timestamp()
delay = int(sys.argv[1])
date1 = datetime.now() - timedelta(days=delay)
print(date1)
