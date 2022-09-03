from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


    

while True:
    secim = input("1-Şarkı Ekle\n2-Çıkış\nSecim:")
    if secim == "2":
        break
    elif secim =="1":
        while True:    
            sarkici = input("Kimden:").lower().strip()
            sarki = input("Hangi şarkı:").lower().strip()
            ifade = f"{sarkici} {sarki}"
            if sarkici =="" or sarki=="":
                break
            else:
                driver = webdriver.Chrome()
                url = "https://www.mp3indirdur.pro"
                driver.get(url)
                driver.find_element_by_xpath("/html/body/div[4]/form/input[1]").send_keys(ifade)
                sleep(4)
                driver.find_element_by_xpath("/html/body/div[4]/form/input[2]").click()
                sleep(4)
                driver.find_element_by_xpath("/html/body/section/a[1]/span").click()
                sleep(3)
                driver.find_element_by_xpath("//*[@id='download']").click()
                
                
                
                print("şarkı indi.")
    else:
       print("yanlış seçim.")



