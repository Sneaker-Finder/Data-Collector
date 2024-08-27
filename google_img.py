from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
name = "hi"
url = "https://www.google.com/search?q={name}&sca_esv=136c67f42ee830f9&udm=2&biw=2048&bih=512&sxsrf=ADLYWILlUCj2E4uW5TXbDhh9_ZaGQwUXzQ%3A1724771401282&ei=SezNZp3wELOhptQP9pLLuA4&ved=0ahUKEwjduMSVupWIAxWzkIkEHXbJEucQ4dUDCBA&uact=5&oq={name}&gs_lp=Egxnd3Mtd2l6LXNlcnAiKE5pa2UtU0ItRHVuay1Mb3ctQmVuLUplcnJ5cy1DaHVua3ktRHVua3lImAZQuANYuANwAXgAkAEAmAF4oAF4qgEDMC4xuAEDyAEA-AEC-AEBmAIBoAJIwgIEECMYJ8ICBBAAGB6YAwCIBgGSBwExoAct&sclient=gws-wiz-serp"
driver.get(url)
time.sleep(2)
results = driver.find_elements(By.XPATH, '//img[@class="YQ4gaf"]')

for result in results:
    print(result.get_attribute('src'))
    break
driver.quit()