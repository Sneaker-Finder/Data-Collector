import requests

def get_images_from_stockx(sneaker_name: str) -> bool:
    """
    Given a 'sneaker_name' saves 36 images of it from StockX.
    Returns true if all 36 successfuly retrieved, false otherwise.
    
    >>> get_images_from_stockx("Timberland-6-Inch-Premium-Waterproof-Wheat")
    True

    """
    sneaker_name = '-'.join(word.capitalize() for word in sneaker_name.split('-'))
    for i in range(1, 37):
        i = "0" + str(i) if i < 10 else i
        img_data = requests.get(f"https://images.stockx.com/360/{sneaker_name}/Images/{sneaker_name}/Lv2/img{i}.jpg")

        if img_data.status_code == 200: 
            img_data = img_data.content
        else: 
            return False
        
        with open(f'{sneaker_name}_#{i}.png', 'wb') as handler:
            handler.write(img_data)
    return True


# Sample Usages
# get_images_from_stockx("Timberland-6-Inch-Premium-Waterproof-Wheat")
# get_images_from_stockx("nike-dunk-low-miami-dolphins")
# get_images_from_stockx("nike-Dunk-Low-concord")
