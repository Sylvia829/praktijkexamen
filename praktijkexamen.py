def bereken_pensioen(leeftijd, statuut):
    basisbedragen = [("medewerker", 350, 20),("zelfstandige", 300, 15),("ambtenaar", 370, 25)]
    for s in basisbedragen:
        if statuut == s[0]:
            if leeftijd >70:
                return s[1] + s[2]
            elif leeftijd>=65:
                return s[1]
            else:
                return None
            
