import calendar
import datetime
import json

today = datetime.datetime.now()
year = today.year

def setDay(day, month):
    month += 1
    if (month == 13):
        month = 1
    max_days = calendar.monthrange(year, month)[1]
    if (day > max_days):
        return [day - max_days, month]
    else:
        return [day, month]
    
def addJson(word: str):
    try:
        with open("addition/json/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                if "admin" in item.get("user", {}):
                    item['user']['admin'][word] += 1
                    with open("addition/json/database.json", 'w', encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
    
    except FileNotFoundError:
        return("File not found")
    except json.JSONDecodeError:
        return("decode error")
    
def setJson(word: str, amount: int):
    try:
        with open("addition/json/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                if "admin" in item.get("user", {}):
                    item['user']['admin'][word] = int(amount)
                    with open("addition/json/database.json", 'w', encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
    
    except FileNotFoundError:
        return("File not found")
    except json.JSONDecodeError:
        return("decode error")

def setDates():
    try:
        with open("addition/json/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                if "admin" in item.get("user", {}):
                    item["user"]["admin"]["start"] = [today.day, today.month]
                    item["user"]["admin"]["end"] = setDay(today.day, today.month)

                    with open("addition/json/database.json", 'w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        return("File not found")
    except json.JSONDecodeError:
        return("decode error")
    
def getData():
    try:
        with open("addition/json/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                if "admin" in item.get("user", {}):
                    start = item["user"]["admin"]["start"]
                    end = item["user"]["admin"]["end"]
                    max = item["user"]["admin"]["max"]
                    current = item["user"]["admin"]["current"]
                    streak = item["user"]["admin"]["streak"]


                    return [start, end, int(max), int(current), int(streak)]

    except FileNotFoundError:
        return("File not found")
    except json.JSONDecodeError:
        return("decode error")

def getJson() -> dict:
    try:
        with open("addition/json/database.json", 'r', encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                if 'admin' in item.get('user', {}):
                    admin_dict = item['user']['admin']
                    max = item['user']['admin']["max"]
                    values = {}
                    for key, value in admin_dict.items():
                        match key:
                            case "start":
                                values["start"] = (f"start at {value[0]} of {calendar.month_name[value[1]]}")
                            case "end":
                                values["end"] = (f"end at {value[0]} of {calendar.month_name[value[1]]}")
                            case "current":
                                values["current"] = (f"currenly {value} out of {max}")
                            case "streak":
                                values["streak"] = (f"current streak is {value}")
    
    except FileNotFoundError:
        return("File not found")
    except json.JSONDecodeError:
        return("decode error")
    return values

