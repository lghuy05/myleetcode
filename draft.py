def eligible_honor_roll(records):
    li = []
    for i in records:
        if i["gpa"] >= 3.5 and i["credits"] >= 12:
            li.append(i["name"])
    li.sort()
    return li


records = [
    {"name": "Ava", "gpa": 3.6, "credits": 15},
    {"name": "Ben", "gpa": 3.4, "credits": 16},
    {"name": "Cara", "gpa": 3.8, "credits": 11},
]
print(eligible_honor_roll(records))
