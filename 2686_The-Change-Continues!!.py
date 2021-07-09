while True:
    try:
        degree = float(input())
        ans = ((degree / 360) * 24)*(60*60)
        degree = degree % 360
        hour = int(ans/3600)
        if hour + 6 == 24:
            hour = '00'
        elif hour + 6 < 10:
            hour = '0'+str(hour+6)
        else:
            hour = str(hour+6)
        min = int(((ans%3600)/60))
        if min < 10:
            min = '0'+str(min)
        else:
            min = str(min)
        sec = int(ans%60)
        if sec < 10:
            sec = '0'+str(sec)
        else:
            sec = str(sec)
        if degree >= 0 and degree < 90:
            print("Bom Dia!!")
            print(hour+':'+min+':'+sec)
        elif degree >= 90  and degree < 180:
            print("Boa Tarde!!")
            print(hour + ':' + min + ':' + sec)
        elif degree >= 180 and degree < 270:
            print("Boa Noite!!")
            print(hour + ':' + min + ':' + sec)
        elif degree >= 270 and degree < 360:
            print("De Madrugada!!")
            print(hour + ':' + min + ':' + sec)
    except EOFError:
        break