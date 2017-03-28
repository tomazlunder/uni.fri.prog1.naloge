__author__ = 'Tomaž Lunder'

counter = 0
stevilo = 1
delitelj = 1
vsota = 0
while counter<4:
    while delitelj<stevilo or (stevilo == 1 and delitelj == 1):
        if stevilo%delitelj == 0:
            vsota+=delitelj
            delitelj+=1
        else:
            delitelj+=1
    if stevilo == vsota:
        print(stevilo)
        counter+=1
        vsota=0
        delitelj=1
        stevilo+=1
    else:
        vsota=0
        delitelj=1
        stevilo+=1

