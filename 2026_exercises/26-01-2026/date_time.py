from datetime import datetime

print("Current D&T:", datetime.now())
print("Date: ", datetime.today())
print("time: ", datetime.now().time())
today = datetime.today()
print("Today", datetime.strftime(today, "%Y-%m-%d"))



date = datetime.strptime("2026-01-01","%Y-%m-%d")
today = datetime.strftime(datetime.today(), "%Y-%m-%d")

print(today)
print(date)