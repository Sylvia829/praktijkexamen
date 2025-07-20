def bereken_pensioen(leeftijd, statuut):
    basisbedragen = [("medewerker", 350, 20),("zelfstandige", 300, 15),("ambtenaar", 370, 25)]
    for s in basisbedragen:
        