import calendar
from datetime import datetime
dt=datetime(2024,10,22,0,0)
print('Datetime to seconds:',calendar.timegm(dt.timetuple()))