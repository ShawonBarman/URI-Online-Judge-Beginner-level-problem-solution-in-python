while True:
    try:
        H = input()
        hour, minute = H.split(":")
        hour = int(hour)
        minute = int(minute)
        if hour>=5 and hour<=9:
            total_minute = hour*60 + minute
            if (total_minute+60) > (8*60):
                total_delay = (total_minute+60) - (8*60)
                print("Atraso maximo: {}".format(total_delay))
            else:
                print("Atraso maximo: {}".format(0))
    except EOFError:
        break