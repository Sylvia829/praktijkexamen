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
            
leeftijd_input = input("Wat is je leeftijd?")
leeftijd = int(leeftijd_input)

statuut = input("Wat is je werkstatuut?")

geldige_statuten = ["medewerker", "zelfstandige", "ambtenaar"]
if statuut not in geldige_statuten:
    print("Ongeldige werkstatuut")
else: 
    pensioen = bereken_pensioen(leeftijd, statuut)
    if pensioen is not None:
        print (f"Je krijgt € {pensioen} per week.")
    else:
        jaren_te_werken = 65 - leeftijd
        print (f"Van werken word je gelukkig, je mag nog {jaren_te_werken} jaar genieten van je baan.")