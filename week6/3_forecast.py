def forecast(days):
    container = {
        "sunshine": 0,
        "rain": 0,
        "snow": 0
        }

    forecast = ""

    for day in days:
        if day == "sunshine":
            container["sunshine"] += 1
        elif day == "rain":
            container["rain"] += 1
        else:
            container["snow"] += 1

    if container["sunshine"] > container["rain"] and container["sunshine"] > container["snow"]:
        forecast = "sunshine"
    elif container["rain"] > container["sunshine"] and container["rain"] > container["snow"]:
        forecast = "rain"
    elif container["snow"] > container["rain"] and container["snow"] > container["sunshine"]:
        forecast = "snow"
    elif container["sunshine"] == container["rain"] and container["sunshine"] > container["snow"]:
        forecast = "snow"
    elif container["sunshine"] == container["snow"] and container["sunshine"] > container["rain"]:
        forecast = "rain"
    elif container["rain"] == container["snow"] and container["rain"] > container["sunshine"]:
        forecast = "sunshine"
    else:
        forecast = days[len(days) - 1]
    
    return forecast
