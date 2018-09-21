# http://www.pythonchallenge.com/pc/return/uzi.html

import calendar
import datetime

years =  [year for year in range(1016, 1996, 20) if datetime.date(year, 1, 26).isoweekday() == 1]
print(years)

# 1756.1.26
# 1756.1.27 is mozart's birthday