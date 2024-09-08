import os
import requests

# def image_converter(image_path):

def shoe_directory_manager():
    with open('shoe_names/valid_shoe_names.txt', 'r') as shoe_names:
        shoe_names =  [shoe.strip() for shoe in shoe_names]

    with open('shoe_names/valid_shoe_names.txt', 'r') as shoe_names:
        shoe_names =  [shoe.strip() for shoe in shoe_names]
    for shoe in shoe_names:
        for i in range(1,37):
            i = "0"+str(i) if i < 10 else i
            image_path = requests.get(f"https://images.stockx.com/360/{shoe}/Images/{shoe}/Lv2/img{i}.jpg")
            with open(f'shoes_directory/{shoe}/{shoe}_#{i}.png', 'wb') as handler:
                handler.write(image_path.content)# Iterate through each subfolder in the main folder
           
                

shoe_directory_manager()