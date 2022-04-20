def open_or_senior(data):
    return ["Senior" if item[0] >= 55 and item[1] > 7 else "Open" for item in data]