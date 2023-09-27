import csv

csv_file_path = "CUAR_JD_NAN_STEP_1_IL_RGB.csv"
output_csv_path = "rgb.csv"


start_point = (1585.0, 6.56)
end_point = (500.0, 2.23)

filtered_points = []

with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Use this flag to skip the first row (header)
    skip_first_row = True

    for row in csv_reader:
        if skip_first_row:
            skip_first_row = False
            continue

        x_str, y_str = map(str.strip, row[0].strip('()').split("/"))
        x, y = int(x_str), float(y_str)

        # if start_point[0] <= x <= end_point[0] and start_point[1] <= y <= end_point[1]:
        filtered_points.append((x, y))

    print(filtered_points)

# Write the filtered points to another CSV file
with open(output_csv_path, "w", newline="") as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(["x", "y"])  # Write header

    for point in filtered_points:
        csv_writer.writerow(point)
