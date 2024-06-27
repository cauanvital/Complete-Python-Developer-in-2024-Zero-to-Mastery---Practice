# You are given a date. Your task is to find what the day is on that date.
# 
# A single line of input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.
#   08 05 2015
# 
# Output the correct day in capital letters.
#   WEDNESDAY

from datetime import datetime

date = datetime.strptime(input(), '%m %d %Y')
print(date.strftime('%A').upper())
