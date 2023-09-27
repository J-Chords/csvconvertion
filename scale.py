import csv
import matplotlib.pyplot as plt

# Path to the CSV dataset file
csv_file_path = "C:/Users/israe/PycharmProjects/zz_test/dataset.csv"  # Update this with your CSV file path

# Lists to store x and y coordinates
x_coords = []
y_coords = []

# Read coordinates from the CSV file
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        x_coords.append(float(row[0]))
        y_coords.append(float(row[1]))

# Create a histogram for x coordinates
plt.figure(figsize=(8, 6))
plt.hist(x_coords, bins=20, color="blue", edgecolor="black")
plt.xlabel("X Coordinate")
plt.ylabel("Frequency")
plt.title("Histogram of X Coordinates")
plt.grid(True)

# Display the histogram
plt.show()

# Create a histogram for y coordinates
plt.figure(figsize=(8, 6))
plt.hist(y_coords, bins=20, color="green", edgecolor="black")
plt.xlabel("Y Coordinate")
plt.ylabel("Frequency")
plt.title("Histogram of Y Coordinates")
plt.grid(True)

# Display the histogram
plt.show()
