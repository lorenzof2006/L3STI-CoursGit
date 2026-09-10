
def calculer_mes_impots(mon_revenu):
    if mon_revenu < 11498:
        return 0
    taux = 0
    if mon_revenu <= 29315:
        taux = 0.11
    elif mon_revenu <= 83823:
        taux = 0.3
    elif mon_revenu <= 180294:
        taux = 0.41
    else:
        taux = 0.45
    return int(mon_revenu*taux)

print(calculer_mes_impots(25000))
print(calculer_mes_impots(200000))
print(calculer_mes_impots(10000))