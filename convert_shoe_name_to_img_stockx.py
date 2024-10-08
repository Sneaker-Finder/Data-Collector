import requests
def get_images_from_stockx(sneaker_name: str, save_image: bool) -> bool:
    """
    Given a 'sneaker_name' saves 36 images of it from StockX if 'save_image' is true, no image saved otherwise.
    Returns true if all 36 successfuly retrieved, false otherwise.
    """
    for i in range(1, 37):
        i = "0" + str(i) if i < 10 else i
        img_data = requests.get(f"https://images.stockx.com/360/{sneaker_name}/Images/{sneaker_name}/Lv2/img{i}.jpg")
        if img_data.status_code == 200: 
            img_data = img_data.content
        else: 
            return False
        if save_image:
            with open(f'{sneaker_name}_#{i}.png', 'wb') as handler:
                handler.write(img_data)
    return True


# Example Usage: 
# print(get_images_from_stockx("Nike-Dunk-Low-Triple-Pink-GS", False))
# get_images_from_stockx("nike-dunk-low-miami-dolphins")
# get_images_from_stockx("nike-Dunk-Low-concord")
