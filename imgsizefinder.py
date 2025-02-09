from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

image_path = "input.png"
width, height = get_image_size(image_path)
print(f"Image size: {width}x{height}")
