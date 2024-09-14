from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import json
import base64

def scrape_google_images_of_shoes_list(shoes_array: list[str])-> None:
    """
    Given an array of shoes 'shoes_array', it searches the web to look for relevant for each shoe. 
    """
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    first_image = '//img[@class="YQ4gaf"]' 
    next_button_path = '//button[@jsname="OCpkoe"]'
    good_image_path = '//img[@class="sFlh5c FyHeAf iPVvYb"]'

    try:
        img_data = {}
        for shoe in shoes_array:

            img_data[shoe] = []
            search_url = "https://www.google.com/search?tbm=isch&q=" + shoe
            driver.get(search_url)
            time.sleep(3)
            first_click = driver.find_element(By.XPATH, first_image)
            first_click.click()
            time.sleep(3)
            
            results = driver.find_elements(By.XPATH, good_image_path)
            
            img_data[shoe].append(results[0].get_attribute('src'))
            prev_shoe = results[0].get_attribute('src')
            
            next_button = driver.find_element(By.XPATH, next_button_path)
            prev_button = next_button.get_attribute('data-ved')

            next_button.click()
            counter = 0
            while (counter < 5):
                time.sleep(2)
                results = driver.find_elements(By.XPATH, good_image_path)
                
                if results != []:
                    prev_shoe = results[0].get_attribute('src')
                for result in results:
                    link = result.get_attribute('src')
                    if link != prev_shoe:
                        img_data[shoe].append(link)
                        print(link)
                        prev_shoe = link
                next_button = driver.find_elements(By.XPATH, next_button_path)
                for buttons in next_button:
                    if buttons.get_attribute('data-ved') != prev_button:
                        prev_button = buttons.get_attribute('data-ved')
                        buttons.click()
                        break
                counter += 1
                
    except:
        print("error occured while retrieving images from google")

    # shoe_url = (img_data[shoes_array[0]][1]).split(",")[1]
    # imgdata = base64.b64decode(shoe_url)
    # with open("test/image.jpg","wb") as f:
    #     f.write(imgdata)
        with open('shoe_img.json', 'w') as file:
            json.dump(img_data, file)
    driver.quit()

# Example usage:
with open('shoe_names/stockx_format_shoes_list.txt', 'r') as shoe_names:
    shoes = [shoe.strip() for shoe in shoe_names]
single = ["Nike-Dunk-Low-Retro-White-Black-2021"]
scrape_google_images_of_shoes_list(shoes)