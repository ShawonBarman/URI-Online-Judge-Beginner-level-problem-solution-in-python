while True:
    try:
        h, m = map(int, input().split())
        hour = int(h/30)
        if hour < 10:
            hour = '0'+str(hour)
        else:
            hour = str(hour)
        minute = int(m/6)
        if minute < 10:
            minute = '0'+str(minute)
        else:
            minute = str(minute)
        print(hour+":"+minute)
    except EOFError:
        break