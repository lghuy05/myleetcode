from datetime import datetime
from dateutil import parser

a = datetime.now()
b = parser.parse(a)
print(b)
