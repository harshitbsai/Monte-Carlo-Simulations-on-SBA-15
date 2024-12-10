# Read the .prp file and calculate the average of Nmols_1 and Pressure

def calculate_averages(file_path):
    nmols_1_values = []
    pressure_values = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into columns and check if it contains numeric data
            columns = line.split()
            if len(columns) == 8:  # Ensure the line contains the expected number of columns
                try:
                    nmols_1 = float(columns[2])  # Nmols_1 is in the 3rd column
                    pressure = float(columns[4])  # Pressure is in the 5th column
                    nmols_1_values.append(nmols_1)
                    pressure_values.append(pressure)
                except ValueError:
                    # Ignore lines where conversion to float fails (likely header lines)
                    pass

    # Calculate the averages
    avg_nmols_1 = sum(nmols_1_values) / len(nmols_1_values) if nmols_1_values else None
    avg_pressure = sum(pressure_values) / len(pressure_values) if pressure_values else None

    return avg_nmols_1, avg_pressure

# Usage example
file_path = 'propane_SBA15_32.out.prp'  # Replace with the actual file path
avg_nmols_1, avg_pressure = calculate_averages(file_path)
print(f"Average Nmols_1: {avg_nmols_1}")
print(f"Average Pressure: {avg_pressure}")

