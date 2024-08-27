from bs4 import BeautifulSoup
from convert_shoe_name_to_img_stockx import get_images_from_stockx


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


def write_shoe_data(shoe_names: list[str], append_file_name: str) -> None:
    """
    Given a list of shoe names 'shoe_names', appends each unique shoe name
    to 'append_file_name' without duplicates. If the file already contains
    some shoe names, the function ensures that the new names are not 
    duplicated in the file.
    """
    try:
        with open(append_file_name, 'r') as file:
            existing_shoes = set(file.read().splitlines())
    except FileNotFoundError:
        print("File has not been found")
        return

    new_shoes = set(shoe_names)
    unique_shoes_to_add = new_shoes - existing_shoes

    with open(append_file_name, 'a') as file:
        for shoe in unique_shoes_to_add:
            file.write(shoe + "\n")


def extracted_name_success_rate(shoes_array: list[str]) -> None:
    """
    Given a list of extracted shoe names 'shoes_array', returns the rate of how many
    of the names are successfully extracted
    """
    success = 0
    fail = 0
    for shoe in shoes_array:
        if get_images_from_stockx(shoe, False):
            success+=1
        else:
            fail+=1
    print("Success: " + str(success), "Fail: " + str(fail))
    print("Success Rate: " + str(success / (success + fail)))

# Example usages:
# shoes_array = extract_shoe_names()
# write_shoe_data(shoes_array, "stockx_format_shoes_list.txt")
# extracted_name_success_rate(shoes_array)