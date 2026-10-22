from datetime import datetime

now = datetime.now()

year = now.strftime("%Y") # Full year
month = now.strftime("%m") # Month as a zero-padded number
day = now.strftime("%d") # Day of the month as a zero-padded number
time = now.strftime("%H:%M:%S") # Hour, minute, second

date_time = now.strftime("%m/%d/%Y, %H:%M:%S") # Combined date and time

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)
print("Date and Time:", date_time)