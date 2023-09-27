from PIL import Image

# Define ASCII characters to use for different pixel intensity levels
ASCII_CHARS = "@%#*+=-:. "

# Convert image to ASCII art
def image_to_ascii(image_path, output_width=100):
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale

    width, height = img.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio)

    img = img.resize((output_width, new_height))
    pixels = img.getdata()

    ascii_image = ""
    for pixel_value in pixels:
        ascii_index = pixel_value * (len(ASCII_CHARS) - 1) // 255
        ascii_image += ASCII_CHARS[ascii_index]

    return ascii_image

# Path to your image
image_path = "born.jpg"

# Convert the image to ASCII art
ascii_art = image_to_ascii(image_path)

# Print or save the ASCII art
print(ascii_art)
