from datetime import*

def diffDate(x):
    skrg = datetime.now()
    skrgX = datetime.date(datetime.now())
    x = x.split("-")
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    date = datetime(year, month, day)
    selisih = date-skrg
    return selisih.days
    
dateX = "2021-12-16"
print("Selisih", diffDate(dateX), "hari.")
