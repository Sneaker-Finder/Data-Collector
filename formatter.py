import requests
from convert_shoe_name_to_img import get_images_from_stockx

removal_characters = ['(',')','.',"'",'"']
root = 'https://stockx.com/'

def check_valid_route(shoe_name):
    url = root+shoe_name
    req = requests.get(url)
    print (req.status_code)


def parse_shoe_data():
    """
    Parses stockx_shoes.txt file to extract all of the shoe names. Returns an array
    with the shoe names cleaned

    """
    with open('stockx_shoes.txt', 'r') as file:
        shoes_array = file.readlines()
        cleaned_array = []
        for line in shoes_array:
            if not (line == '\n' or "$" in line or 'Xpress Ship' in line or 'Lowest Ask' in line or 'sold' in line or line in cleaned_array):
                line = line.strip().replace(" ", "-").lower()
                for char in removal_characters:
                    line = line.replace(char,'')
                if(line not in cleaned_array):
                    cleaned_array.append(line)
    return cleaned_array

def write_shoe_data(shoe_names):
    """
    Given array of shoe names 'shoe_names', creates a .txt file where each line is
    a shoe name in 'shoe_names'. 

    """
    with open('cleaned_stockx_shoes.txt', 'w') as file:
        for shoe in shoe_names:
            file.write(shoe+"\n")

shoe_array = parse_shoe_data()
write_shoe_data(shoe_array)
