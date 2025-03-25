import csv
from datetime import datetime

with open("ApplicationLog.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row.get("Type") == "Universal Print":
            timestamp = row.get("DateTime")
            try:
                dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                print("{:>6}".format(dt.hour) + ":" + "{:>6}".format(dt.second) + "\t" +
                      "{:>6}".format(dt.day) + ":" + "{:>6}".format(dt.month) + ":" + "{:>6}".format(dt.year))
            except ValueError:
                print("Invalid datetime format: " + timestamp)