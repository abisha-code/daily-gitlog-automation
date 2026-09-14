import datetime
import os

today = datetime.date.today().isoformat()
log_path = "activity_log.md"

entry = f"- {today}: Daily automated check-in\n"

if os.path.exists(log_path):
    with open(log_path, "r") as f:
        content = f.read()
    if today in content:
        print("Already logged today, skipping.")
        exit(0)
else:
    content = "# Activity Log\n\n"

with open(log_path, "w") as f:
    f.write(content + entry)

print("Log updated.")
