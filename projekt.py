from tkinter import *
from tkinter import ttk

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

def leia_valiku_parameetrid(sõnastik, sammu_võti, valiku_võti):
    sammu_jär = sõnastik[sammu_võti]
    valiku_dict = sammu_jär[2]
    valiku_jär = valiku_dict[valiku_võti]
    ressurss = valiku_jär[1]
    ressursi_mõju = valiku_jär[2]
    lõpu_tüüp = valiku_jär[3]
    järgmine_samm = valiku_jär[4]
    return = ressurss, ressursi_mõju, lõpu_tüüp, järgmine_samm

def järgmise_sammu_parameetrid(sõnastik, järgmine_samm):
    järgmise_sammu_jär = sõnastik[järgmine_samm]
    tekst = järgmise_sammu_jär[0]
    pilt = järgmise_sammu_jär[1]
    valiku_dict = järgmise_sammu_jär[2]
    a_valik_jär = valiku_dict[A]
    a_tekst = a_valik_jär[0]
    b_valik_jär = valiku_dict[B]
    b_tekst = b_valik_jär[0]
    return tekst, pilt, a_tekst, b_tekst

def arvuta_ressurss_ja_lõpp(ressurss, ressursi_mõju, lõpu_tüüp, parim_lõpp_kokku, hea_lõpp_kokku, aega_alles, raha_alles):
    if ressurss == "aeg":
        aega_alles -= ressursi_mõju
    elif ressurss == "raha":
        raha_alles -= ressursi_mõju
    if lõpu_tüüp == "parim":
        parim_lõpp_kokku += 1
    elif lõpu_tüüp == "hea":
        hea_lõpp_kokku += 1
    return aega_alles, raha_alles, parim_lõpp_kokku, hea_lõpp_kokku

#kasutaja valib sammu 1 valiku a -> leiab valiku a järjendi -> leiab valiku a järjendist ressurss,
#ressursi_mõju, lõpu_tüüp, järgmine_samm -> lahutab ja uuendab ressursi -> summeerib lõpu ->
#leiab järgmise sammu teksti, pildi ja valikute teksti -> uuendab akent järgmisele sammule

raha_alles = 10
aega_alles = 10
parim_lõpp_kokku = 0
hea_lõpp_kokku = 0

------------------------------WIP-------------------------------------------------
root = Tk()
ttk.title("Test")
# three pixels at the left and top, 12 pixels at the right and bottom
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#label = ttk.Label(mainframe, text = "kirjeldav tekst")
#resultsContents = StringVar()
#label["textvariable"] = resultsContents
#resultContents.set("tekst sõnastikust")
#resultContents.grid(column=1, row=1, sticky=(W))

ttk.Label(mainframe, text = "kirjeldav tekst").grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text = "Aeg:").grid(column=1, row=4, sticky=(W))
ttk.Label(mainframe, text = "Raha:").grid(column=1, row=5, sticky=(W))

#compound right: config option, image to right of text
#image = PhotoImage(file = ...)
#label["image"] = image
PhotoImage(mainframe, file = ...).grid(column=3, row=2, sticky=(E))

ttk.Button(mainframe, text = "Edasi", command = submitForm).grid(column=2, row=3, sticky=(S))

valik = StringVar()
ttk.RadioButton(mainframe, text="valik a", variable = valik, value = "valik a").grid(column=1, row=2, sticky=(S, E))
ttk.RadioButton(mainframe, text="valik b", variable = valik, value = "valik b").grid(column=1, row=3, sticky=(S, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()