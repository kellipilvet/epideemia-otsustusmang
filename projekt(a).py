from tkinter import *
from tkinter import ttk


#FUNKTSIOONID#
def failist_sõnastikku(failinimi):
    """Loeb küsimused tekstifailist ja salvestab need sõnastikku."""
    sõnastik = {}

    with open(failinimi, "r", encoding="utf-8") as fail:
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


def leia_valiku_parameetrid(sõnastik, sammu_võti, valiku_võti):
    """Leiab valitud vastuse ressursimuutused ja järgmise sammu."""
    sammu_jär = sõnastik[sammu_võti]
    valiku_dict = sammu_jär[2]
    valiku_jär = valiku_dict[valiku_võti]

    muudatused = valiku_jär[1:-1]
    järgmine_samm = valiku_jär[-1]

    return muudatused, järgmine_samm


def arvuta_ressursid(ressursid, muudatused):
    """Muudab mängija ressursse vastavalt valitud vastusele."""
    for i in range(0, len(muudatused), 2):
        ressurss = muudatused[i]
        mõju = int(muudatused[i + 1])
        ressursid[ressurss] += mõju

    return ressursid


def kontrolli_ressursse(ressursid):
    """Kontrollib, kas mängijal on raha ja aega jäänud."""
    if ressursid["raha"] <= 0:
        return False
    elif ressursid["aeg"] <= 0:
        return False
    else:
        return True


def määra_lõpp(ressursid):
    """Määrab mängu lõpu mängija ressursside põhjal."""
    if kontrolli_ressursse(ressursid) == False:
        return "halb lõpp"

    tulemus = 0
    for ressurss in ressursid:
        tulemus += ressursid[ressurss]

    if tulemus >= 32:
        return "parim lõpp"
    elif tulemus >= 29:
        return "hea lõpp"
    else:
        return "halb lõpp"


def järgmise_sammu_parameetrid(sõnastik, järgmine_samm):
    """Leiab järgmise küsimuse teksti, pildi ja vastusevariandid."""
    järgmise_sammu_jär = sõnastik[järgmine_samm]

    tekst = järgmise_sammu_jär[0]
    pilt = järgmise_sammu_jär[1]

    valiku_dict = järgmise_sammu_jär[2]

    a_valik_jär = valiku_dict["A"]
    a_tekst = a_valik_jär[0]

    b_valik_jär = valiku_dict["B"]
    b_tekst = b_valik_jär[0]

    return tekst, pilt, a_tekst, b_tekst


def edasi():
    """Liigub mängija valiku järgi järgmise küsimuse juurde."""
    global praegune_samm

    if valik.get() == "":
        return

    muudatused, järgmine_samm = leia_valiku_parameetrid(
        küsimused, praegune_samm, valik.get())
    
    arvuta_ressursid(ressursid, muudatused)
    näita_ressursse()
    
    if kontrolli_ressursse(ressursid) == False:
        näita_lõppu()
        return

    if järgmine_samm == "LÕPP":
        näita_lõppu()
        return

    praegune_samm = järgmine_samm

    tekst, pilt, a_tekst, b_tekst = järgmise_sammu_parameetrid(
        küsimused, praegune_samm)

    küsimuse_tekst.config(text=tekst)
    a_nupp.config(text=a_tekst)
    b_nupp.config(text=b_tekst)

    valik.set("")
    

def näita_lõppu():
    """Näitab mängu lõpptulemust aknas."""
    lõpp = määra_lõpp(ressursid)

    küsimuse_tekst.config(text=lõpp)
    a_nupp.grid_remove()
    b_nupp.grid_remove()
    edasi_nupp.grid_remove()
    
    
def näita_ressursse():
    """Näitab mängija ressursse aknas."""
    tekst = "Raha: " + str(ressursid["raha"])
    tekst += " | Aeg: " + str(ressursid["aeg"])
    tekst += " | Tarkus: " + str(ressursid["tarkus"])
    tekst += " | Tervis: " + str(ressursid["tervis"])
    tekst += " | Karisma: " + str(ressursid["karisma"])

    ressursside_tekst.config(text=tekst)


#PÕHIPROGRAMM#
küsimused = failist_sõnastikku("tekstifail.txt")

ressursid = {
    "raha": 20,
    "aeg": 5,
    "tarkus": 0,
    "tervis": 1,
    "karisma": 0
}


#MÄNGUAKEN#
praegune_samm = "1"
root = Tk()
root.title("Epideemia otsustusmäng")

mainframe = ttk.Frame(root, padding=20)
mainframe.grid(row=0, column=0)

tekst, pilt, a_tekst, b_tekst = järgmise_sammu_parameetrid(küsimused, praegune_samm)

#ttk.Label(mainframe, text="Epideemia otsustusmäng").grid(row=0, column=0)

küsimuse_tekst = ttk.Label(mainframe, text=tekst, wraplength=700)
küsimuse_tekst.grid(row=1, column=0)

valik = StringVar()

a_nupp = ttk.Radiobutton(mainframe, text=a_tekst, variable=valik, value="A")
a_nupp.grid(row=2, column=0)

b_nupp = ttk.Radiobutton(mainframe, text=b_tekst, variable=valik, value="B")
b_nupp.grid(row=3, column=0)

edasi_nupp = ttk.Button(mainframe, text="Edasi", command=edasi)
edasi_nupp.grid(row=4, column=0)

ressursside_tekst = ttk.Label(mainframe, text="")
ressursside_tekst.grid(row=5, column=0)
näita_ressursse()

root.mainloop()



# #KONTROLL_PLOKK#
# 
# #1. funkts
# print(len(küsimused)) 
# print(küsimused["9"][2]["A"]) 
# 
# #2. funkts
# muudatused, järgmine_samm = leia_valiku_parameetrid(küsimused, "7", "A") 
# print(muudatused) 
# print(järgmine_samm)
# 
# #3. funkts
# ressursid = {
#     "raha": 20,
#     "aeg": 5,
#     "tarkus": 0,
#     "tervis": 1,
#     "karisma": 0
# }
# print("Enne:", ressursid)
# arvuta_ressursid(ressursid, muudatused)
# print("Pärast:", ressursid)
# print("Järgmine samm:", järgmine_samm)
# 
# #4. funkts
# print(kontrolli_ressursse(ressursid))
# ressursid["raha"] = 0
# print(kontrolli_ressursse(ressursid))
# 
# ressursid["raha"] = 20
# ressursid["aeg"] = 0
# print(kontrolli_ressursse(ressursid))
# 
# #5. funkts
# ressursid = {
#     "raha": 20,
#     "aeg": 5,
#     "tarkus": 0,
#     "tervis": 1,
#     "karisma": 0
# }
# 
# print(määra_lõpp(ressursid))
# ressursid["raha"] = 10
# print(määra_lõpp(ressursid))
# ressursid["aeg"] = 0
# print(määra_lõpp(ressursid))
# 
# #6. funkts
# tekst, pilt, a_tekst, b_tekst = järgmise_sammu_parameetrid(küsimused, "1")
# 
# print("Küsimus:", tekst)
# print("Pilt:", pilt)
# print("A:", a_tekst)
# print("B:", b_tekst)

# #7. funkts
# print("Praegune samm:", praegune_samm)
# print("Ressursid:", ressursid)
