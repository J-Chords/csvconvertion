import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv


# Encode CSV data to an image
def csv_to_image(input_csv, output_image):
    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        image_data = []
        for row in csv_reader:
            image_data.append([int(val) for val in row])

        image = Image.new('L', (len(image_data[0]), len(image_data)))
        for y, row in enumerate(image_data):
            for x, val in enumerate(row):
                image.putpixel((x, y), val)

        image.save(output_image)


# Decode an image to CSV data
def image_to_csv(input_image, output_csv):
    image = Image.open(input_image)
    csv_data = []
    for y in range(image.height):
        row = []
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            row.append(str(pixel))
        csv_data.append(row)

    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)


# GUI
class ImageCSVConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image <-> CSV Converter")

        self.file_label = tk.Label(root, text="Choose a CSV file:")
        self.file_label.pack()

        self.file_button = tk.Button(root, text="Browse", command=self.choose_csv)
        self.file_button.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def choose_csv(self):
        self.csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    def convert(self):
        if hasattr(self, 'csv_file_path'):
            output_image_path = self.csv_file_path.replace(".csv", ".png")
            csv_to_image(self.csv_file_path, output_image_path)
            self.show_image(output_image_path)
            self.convert_button.config(text="Convert Back", command=self.convert_back)
        else:
            self.file_label.config(text="Choose a CSV file first!")

    def convert_back(self):
        if hasattr(self, 'csv_file_path'):
            output_csv_path = self.csv_file_path.replace(".csv", "_back.csv")
            image_to_csv(output_image_path, output_csv_path)
            self.file_label.config(text="CSV file converted back!")

    def show_image(self, image_path):
        image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.image = self.photo
        self.image_label.pack()


root = tk.Tk()
app = ImageCSVConverterApp(root)
root.mainloop()
