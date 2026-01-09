from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

with open("daily_log.txt", "a") as file:
    file.write(f"Daily commit on {today}\n")

print("Committed for", today)
