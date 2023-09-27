from PIL import Image
import os

# Replace 'image.jpg' with the actual image file name on your desktop
image_path = os.path.expanduser("C:/Users/israe/PycharmProjects/zz_test/born.jpg")

try:
    img = Image.open(image_path)
    img.show()
except Exception as e:
    print(f"Error: {e}")
