
def conversion_masse(val,unite_dep,unite_arr):
    # On choisi de représenter les unités par les puissances de 10
    unites = {
    "mg": 0.001,
    "cg": 0.01,
    "dg": 0.1,
    "g": 1,
    "dag": 10,
    "hg": 100,
    "kg": 1000
}
    if unite_dep not in unites or unite_arr not in unites:
        return "Unites non connues"    
    unite_dep = unites[unite_dep]
    unite_arr = unites[unite_arr]
    return val * unite_dep / unite_arr

print(conversion_masse(45, "kg", "g"))
print(conversion_masse(45, "g", "kg"))
print(conversion_masse(45, "mg", "hg"))
print(conversion_masse(45, "kilo", "g"))