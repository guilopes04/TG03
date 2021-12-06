from datetime import *

data = datetime.date(2021, 12, 6)
print(data)
data = '{}/{}/{}'.format(data.day, data.month, data.year)
print(data)