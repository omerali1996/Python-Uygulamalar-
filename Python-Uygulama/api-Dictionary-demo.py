import requests
import json
import re
class Dictionary:
    def __init__(self):
        self.api_key = "dict.1.1.20200521T101424Z.c25d538b2bf5141e.9c9dc3bf548445ae8b3a3eebdb7cc6ce4e17ec98"
    def English(self,kelime):
        self.kelime = kelime
        response = requests.get(f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={self.api_key}&lang=en-tr&text={self.kelime}').json()
        return response
    def getLang(self):
        response = requests.get("https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key={}".format(self.api_key))
        x = response.json()
        y = 0
        z = 13 
        while z <= 105:
          print(x[y:z])
          y +=13
          z +=13
        
    def show(self,dil,kelime):
        self.dil = dil
        self.kelime = kelime
        response = requests.get(f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={self.api_key}&lang={self.dil}&text={self.kelime}')
        return response.json()
    
    def findLang(self):
        list = ["tr-Türkçe","en-İngilizce","fr-Fransızca","es-İspanyolca","it-İtalyanca","ru-Rusça",
        "de-Almanca","nl-Flemenkçe","bg-Bulgarca"]
        for dil in list:
            print(dil)        

dict = Dictionary()
while True:
     
    print("MENÜ".center(12,"*"))
    secim = input("1- Çeviri\n2- Yaygın Kullanılan Dil Kodları\n3- İngilizce-Türkçe\n4- Exit\nSecim: ").strip()
    if secim =="4":
        break
    else:
        if secim =="1":
            print("Dil formatı için 'Mevcut Diller' kısmındaki yazı formatını kullanınız.")
            print("*"*5)
            gecis=input("'Mevcut Diller' kısmına geçiş yapmak için 1'e basın veya işleme devam etmek için  -çeviri- yazın veya 2'ye basın => ").lower().strip()
            if gecis =="1":
                dict.getLang()
            elif gecis == 'çeviri' or gecis == "2":
                dil = input("dil formatı girin:").strip().lower()
                kelime = input("kelime:").strip().lower()
                try:
                    cevap = dict.show(dil,kelime)
                    list = []
                    for cevap in cevap["def"]:
                        for cevap in cevap["tr"]:
                            list.append(cevap["text"])    
                    print(list)
                except Exception as hata:
                    print("!! Seçilen diller arası çeviri mevcut değil !!")
            else:
                print("!! Hatalı Tercih !!".center("*",5))    
        
        elif secim =="2":
            dict.findLang()
        
        elif secim =="3":
            while True:
                kelime = input("kelime:").strip()
                if kelime == "":
                    break
                else:
                    list =[]
                    cevap = dict.English(kelime)
                    for cevap in cevap["def"]:
                        for cevap in cevap["tr"]:
                            list.append(cevap["text"])
                    print(list)    
        else:
            print("!! Yanlış Seçim!!")