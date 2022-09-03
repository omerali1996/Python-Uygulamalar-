from bs4 import BeautifulSoup
import requests
def Discount():
    html = requests.get("https://store.steampowered.com/specials#&tab=TopSellers").content
    soup = BeautifulSoup(html,"html.parser").find("div",{"id":"TopSellersRows"}).find_all("a")
    count = 0
    for oyun in soup:
        oyunadi = oyun.find("div",{"class":"tab_item_name"}).text
        fiyat =  oyun.find("div",{"class":"discount_original_price"}).text
        indirimlifiyat = oyun.find("div",{"class":"discount_final_price"}).text
        count += 1
        print(f"{count}- {oyunadi.ljust(70)} fiyatı {fiyat} değerinden {indirimlifiyat} olmuştur.")

Discount()