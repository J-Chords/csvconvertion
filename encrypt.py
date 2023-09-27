import csv

# Encoding function for each digit (D)
def A(D):
    return 23 * D + 13

# Encode Y coordinate into pixels
def encode_y(y):
    y *= 1000  # Multiply by 1000 to handle decimal point

    y_str = str(y)
    y_str = y_str.replace('.', '').ljust(5, '0')  # Remove decimal point and pad to 5 digits

    pixels = []
    for char in y_str:
        if char == '2':
            pixels.append(2)  # Attenuation for decimal point indicator

        digit = int(char)
        attenuation = A(digit)
        pixels.append(attenuation)

    # Add 8 to indicate the end of the Y value
    pixels.append(8)

    return pixels

# Encode CSV data and create pixel representation
def encode_csv(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        next(reader)  # Skip the header row

        for row in reader:
            x = row[0]
            y_str = row[1]
            encoded_y = encode_y(float(y_str.replace('.', '2')))

            writer.writerow([x] + encoded_y)

if __name__ == "__main__":
    input_csv = "rgb.csv"
    output_csv = "a.csv"

    encode_csv(input_csv, output_csv)
    print("Data encoded and saved to output.csv")
