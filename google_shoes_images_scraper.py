from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import json

def scrape_google_images_of_shoes_list(shoes_array: list[str])-> None:
    """
    Given an array of shoes 'shoes_array', it searches the web to look for relevant for each shoe. 
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    google_class_name = "YQ4gaf"

    try:
        img_data = {}
        for shoe in shoes_array:
            img_data[shoe] = []
            search_url = "https://www.google.com/search?tbm=isch&q=" + shoe
            driver.get(search_url)
            time.sleep(3)
            results = driver.find_elements(By.XPATH, '//img[@class="YQ4gaf"]')
            print(shoe)
            for result in results[2:12]:
                print(result.get_attribute('src'))
                img_data[shoe].append(result.get_attribute('src'))
    except:
        print("error occured while retrieving images from google")


    with open('shoe_img.json', 'w') as file:
        json.dump(img_data, file)
    driver.quit()

# Example usage:
with open('static resources/stockx_format_shoes_list.txt', 'r') as shoe_names:
    shoes = [shoe.strip() for shoe in shoe_names]
# single = ["Nike-Dunk-Low-Retro-White-Black-2021"]
scrape_google_images_of_shoes_list(shoes)