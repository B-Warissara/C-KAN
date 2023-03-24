#pip install python-dateutil
from datetime import datetime , date
from dateutil.relativedelta import relativedelta

def demol():
    now = datetime.today()
    today = date.today()
    next_3_m = today + relativedelta(years = 3) #chang years,months,days
    print(today)
    print(next_3_m)

demol()