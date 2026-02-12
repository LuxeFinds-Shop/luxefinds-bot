lager = {
    "50K Vape": {"preis": 25, "menge": 10, "kategorie": "Vapes"},
    "60K Vape": {"preis": 30, "menge": 10, "kategorie": "Vapes"},
}

def alle():
    return lager

def holen(name):
    return lager.get(name, {})

def reduzieren(name, menge):
    if name in lager:
        lager[name]["menge"] -= menge

def erhoehen(name, menge):
    if name in lager:
        lager[name]["menge"] += menge
