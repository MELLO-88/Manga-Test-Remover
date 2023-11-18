from PIL import Image

def get_image_width(image_path):
    image = Image.open(image_path)
    width = image.width
    return width * 0.045

def get_image_height(image_path):
    image = Image.open(image_path)
    height = image.height
    return height * 0.016