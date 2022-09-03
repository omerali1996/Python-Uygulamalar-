from bs4 import BeautifulSoup
import requests
def FindMean(kelime):
    html = requests.get("https://tr.bab.la/sozluk/almanca-turkce/{}".format(kelime)).content
    soup = BeautifulSoup(html,"html.parser")
    anlam = soup.find("ul",{"class":"sense-group-results"}).find("li").text
    ifade = soup.find("a",{"class":"babQuickResult"}).text
    artikel = soup.find("span",{"class":"suffix"}).text.strip("{}").strip(".")
    if artikel == "diş":
        artikel = "die"
    elif artikel == "nö":
        artikel = "das"
    elif artikel =="er":
        artikel = "der"  
    elif artikel =="fi":
        artikel = "fiil"
    elif artikel =="sıf":
        artikel="sıfat"
    elif artikel =="ed":
        artikel="edat"
    elif artikel =="zam":
        artikel= "zamir"
    elif artikel =="bağ":
        artikel ="bağlaç"
    print(f"<< {ifade.upper()} >>  ==> {anlam} , TANIMLIK ==> {artikel}")
def Fiil(kelime):
    html = requests.get("https://tr.bab.la/fiil-cekimi/almanca/{}".format(kelime)).content
    soup = BeautifulSoup(html,"html.parser")
    fiil = soup.find("ul",{"class":"sense-group-results"}).find("li").text
    print(f"MASTAR HAL ==> {fiil}")
def Prasens(kelime):
    html = requests.get("https://tr.bab.la/fiil-cekimi/almanca/{}".format(kelime)).content
    soup = BeautifulSoup(html,"html.parser")
    list = soup.find("div",{"class":"conj-tense-block"}).find_all("div",{"class":"conj-item"},limit = 6) 
    for fiil in list:
        kisi = fiil.find("div",{"class":"conj-person"}).text
        cekim = fiil.find("div",{"class":"conj-result"}).text
        print(f"{kisi.ljust(15)} =======> {cekim}")

def Prateritum(kelime):
    html = requests.get("https://tr.bab.la/fiil-cekimi/almanca/{}".format(kelime)).content
    soup = BeautifulSoup(html,"html.parser")
    list = soup.find("div",{"class":"conj-tense-block"}).findNextSibling().find_all("div",{"class":"conj-item"},limit = 6) 
    for fiil in list:
        kisi = fiil.find("div",{"class":"conj-person"}).text
        cekim = fiil.find("div",{"class":"conj-result"}).text
        print(f"{kisi.ljust(15)} =======> {cekim}")

def Perfekt(kelime):
    html = requests.get("https://tr.bab.la/fiil-cekimi/almanca/{}".format(kelime)).content
    soup = BeautifulSoup(html,"html.parser")
    list = soup.find("div",{"class":"conj-tense-block"}).findNextSibling().findNextSibling().find_all("div",{"class":"conj-item"},limit = 6) 
    for fiil in list:
        kisi = fiil.find("div",{"class":"conj-person"}).text
        cekim = fiil.find("div",{"class":"conj-result"}).text
        print(f"{kisi.ljust(15)} =======> {cekim}")


  
while True:
    secim = input("1-Kelime Avı\n2-Fiil Çekimi\n3-Çıkış\nSecim:")
    if secim =="3":
        break
    elif secim =="2":
        while True:
            kelime = input("fiil:").strip().lower()
            if kelime =="":
                break
            else:
                try:
                    print("--------")
                    Fiil(kelime)
                    print("PRASENS HALLER")
                    Prasens(kelime)
                    print("PERFEKT HALLER")
                    Perfekt(kelime)
                except Exception as hata:
                    print("Girilen fiil yanlış veya hatalı")
    elif secim =="1":
        while True:
            kelime = input("kelime:").strip().lower()
            if kelime =="":
                break
            else:
                try:
                    FindMean(kelime)
                except Exception as hata:
                    print("Girilen kelime yanlış veya hatalı")
    else:
        print("yanlış seçim!!")