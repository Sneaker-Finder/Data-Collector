from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import json
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

google_class_name = "YQ4gaf"
file = open('stockx_shoes.txt', 'r')
shoes = []
for line in file:
    shoes.append(line.strip())
file.close()

try:
    img_data = {}
    for shoe in shoes:
        img_data[shoe] = []
        url = "https://www.google.com/search?q="+ shoe+ "&sca_esv=136c67f42ee830f9&udm=2&biw=2048&bih=512&sxsrf=ADLYWILlUCj2E4uW5TXbDhh9_ZaGQwUXzQ%3A1724771401282&ei=SezNZp3wELOhptQP9pLLuA4&ved=0ahUKEwjduMSVupWIAxWzkIkEHXbJEucQ4dUDCBA&uact=5&oq="+shoe+"&gs_lp=Egxnd3Mtd2l6LXNlcnAiKE5pa2UtU0ItRHVuay1Mb3ctQmVuLUplcnJ5cy1DaHVua3ktRHVua3lImAZQuANYuANwAXgAkAEAmAF4oAF4qgEDMC4xuAEDyAEA-AEC-AEBmAIBoAJIwgIEECMYJ8ICBBAAGB6YAwCIBgGSBwExoAct&sclient=gws-wiz-serp"
        driver.get(url)
        time.sleep(3)
        results = driver.find_elements(By.XPATH, '//img[@class="YQ4gaf"]')
        print(shoe)
        for result in results:
            img_data[shoe].append(result.get_attribute('src'))
except:
    print("error occured")


with open('shoe_img.json', 'w') as file:
    json.dump(img_data, file)
driver.quit()