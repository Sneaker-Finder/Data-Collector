from bs4 import BeautifulSoup
from convert_shoe_name_to_img import get_images_from_stockx

def format_shoe_name(shoe_name,actual):
    formatted_name = []
    for word in shoe_name.split("-"):
        if word.upper() in actual:
            formatted_name.append(word.upper())
        else:
            formatted_name.append(word.capitalize())
    return "-".join(formatted_name)

def extract_shoe_names():
    shoe_names_array = []
    for i in range (0,25):
        with open(f'stockx_pages/formatted ({i}).html', 'r') as file:
            contents = file.read()
            soup = BeautifulSoup(contents, 'html.parser')
            full_shoe_names = [p.getText() for p in soup.find_all('p') if 'Lowest Ask' not in p.getText() and 'CA$' not in p.getText()]
            for div,p in zip(soup.find_all('div',attrs={'data-testid':'productTile'}),full_shoe_names):
                shoe_name_formatted =format_shoe_name( div.find('a')['href'][1:],p)
                shoe_names_array.append(shoe_name_formatted)
    return shoe_names_array

def write_shoe_data(shoe_names):
    """
    Given array of shoe names 'shoe_names', creates a .txt file where each line is
    a shoe name in 'shoe_names'. 

    """
    with open('stockx_shoes.txt', 'w') as file:
        for shoe in shoe_names:
            file.write(shoe+"\n")

shoes_array = extract_shoe_names()
# write_shoe_data(shoes_array)
# success = 0
# fail = 0
# for shoe in shoes_array:
#     if get_images_from_stockx(shoe):
#         success+=1
#     else:
#         fail+=1
