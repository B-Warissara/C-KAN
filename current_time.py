from datetime import datetime
from datetime import date

# get current date and time
now = datetime.today()

# display using difference formats
print(now)
print(now.isoformat())
print(now.ctime())