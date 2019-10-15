import json
import os
import pprint as pp
import re

READFILE = "_data/Coders_gonna_code.txt"

# 14/10/2019, 18:38 - Luc Hayward: This message was deleted
re_date = re.compile(r"(\d{2}/\d{2}/\d{4})")
re_time = re.compile(r"(\d{2}:\d{2})")
re_person = re.compile(r"(?<= - )(.*)(?=: )")
re_message = re.compile(r"(?<=: )(.*)")

people = {}

with open(READFILE, "r") as textfile:
    for i, line in enumerate(textfile):
        person = re.search(re_person, line)
        date = re.search(re_date, line)
        time = re.search(re_time, line)
        message = re.search(re_message, line)

        person = person.group() if person else "UNKOWN PERSON"
        message = message.group() if message else line
        date = date.group() if date else "UNKOWN DATE"
        time = time.group() if time else "UNKOWN TIME"

        if person not in people.keys():
            people[person] = [{
                "date": date,
                "time": time,
                "message": message
            }]
        else:
            people[person].append({
                "date": date,
                "time": time,
                "message": message
            })

# pp.pprint(people)
for name in people.keys():
    pp.pprint(name)
    # filepath = f"{name}.json"
    # if os.path.exists(filepath):
    #     with open(filepath, "w") as writefile:
    #         json.dump(people[name], writefile, indent="  ")
    # else:
    #     with open(filepath, "x") as writefile:
    #         json.dump(people[name], writefile, indent="  ")
