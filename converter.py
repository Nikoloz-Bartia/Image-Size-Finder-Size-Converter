from PIL import Image

def resize_image(input_path, output_path, size):

    with Image.open(input_path) as img:
        img_resized = img.resize(size, Image.LANCZOS)
        img_resized.save(output_path)
        print(f"Image saved to {output_path}")

# Example usage:
resize_image("input.png", "traning.png", (572, 360))
