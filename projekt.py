#import tkinter

def failist_sõnastikku(failinimi):
    sõnastik = {}
    with open(failinimi, "r", encoding = "UTF-8") as fail:
        while True:
            samm = fail.readline().strip()
            if not samm:
                break
            kirjeldav_tekst = fail.readline().strip()
            pilt = fail.readline().strip()
            valik_a = fail.readline().strip().split(";")
            valik_b = fail.readline().strip().split(";")
            
            valiku_sõnastik = {}
            valiku_sõnastik[valik_a[0]] = valik_a[1:]
            valiku_sõnastik[valik_b[0]] = valik_b[1:]
            
            järjend = [kirjeldav_tekst, pilt, valiku_sõnastik]
            
            sõnastik[samm] = järjend
    return sõnastik

print(failist_sõnastikku("test.txt"))