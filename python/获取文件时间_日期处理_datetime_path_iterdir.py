import time
import os
import arrow
import datetime
def fileTime(file):
    return [
        time.ctime(os.path.getatime(file)),
        time.ctime(os.path.getmtime(file)),
        time.ctime(os.path.getctime(file))
    ]

times = fileTime(os.getcwd())
print(os.getcwd())
print(times)
print(type(times))
d1 = datetime.datetime.strptime('2015-03-05', '%Y-%m-%d')
from pathlib import Path
p = Path(r"d:\py")
for i in p.iterdir():
  print(i,arrow.get(os.path.getatime(i))>arrow.get('2022-03-01'))

import datetime
d1 = datetime.datetime.strptime('2015-03-05', '%Y-%m-%d')
d2 = datetime.datetime.strptime('2015-03-02', '%Y-%m-%d')
vv=d2-d1
print(vv)

