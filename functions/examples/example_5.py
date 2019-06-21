import datetime

def greetings():
    now = datetime.datetime.now()
    hour = now.hour
    if hour <= 11 and hour >= 3:
        return 'Good morning'
    elif hour >= 12 and hour <= 18:
        return 'Good afternoon'
    elif hour >= 19 and hour <= 21:
        return 'Good evening'
    else:
        return 'Good night'


print(greetings())