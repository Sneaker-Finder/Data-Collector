import os
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import base64

def get_shoe_names()-> None:
    with open('shoe_names/valid_shoe_names.txt', 'r') as shoe_names:
        return [shoe.strip() for shoe in shoe_names]
    
def shoe_directory_manager()-> None:
    shoe_names = get_shoe_names()

    with open('shoe_names/valid_shoe_names.txt', 'r') as shoe_names:
        shoe_names =  [shoe.strip() for shoe in shoe_names]
    for shoe in shoe_names:
        for i in range(1,37):
            i = "0"+str(i) if i < 10 else i
            image_path = requests.get(f"https://images.stockx.com/360/{shoe}/Images/{shoe}/Lv2/img{i}.jpg")
            with open(f'shoes_directory/{shoe}/{shoe}_#{i}.png', 'wb') as handler:
                handler.write(image_path.content)

def convert_google_img_to_file()-> None:
    shoes_array = get_shoe_names()

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # google_class_name = "YQ4gaf"


    for shoe in ["Nike-Kobe-6-Protro-Reverse-Grinch"]:
        base64_shoe_codes = []
        search_url = "https://www.google.com/search?tbm=isch&q=" + " ".join(shoe.split("-"))
        print(search_url)
        driver.get(search_url)

        time.sleep(2)
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        results = driver.find_elements(By.XPATH, '//img[@class="YQ4gaf"]')
        
        for result in results[2:52]:
            base64_shoe_codes.append(result.get_attribute('src'))
        i = 0
        for url in base64_shoe_codes:
            try:
                shoe_url = url.split(",")[1]
                imgdata = base64.b64decode(shoe_url)
                with open(f"test/{shoe}_{i}.png","wb") as f:
                    f.write(imgdata)
            except:
                print("error occured while retrieving images from google: "+url)
            i+=1
            
    

    driver.quit()
    
convert_google_img_to_file()
# shoe_directory_manager()