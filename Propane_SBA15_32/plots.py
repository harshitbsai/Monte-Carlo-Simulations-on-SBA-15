import matplotlib.pyplot as plt

def calculate_averages_and_save_plot(file_path, output_image_path):
    mc_steps = []
    nmols_1_values = []
    pressure_values = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into columns and check if it contains numeric data
            columns = line.split()
            if len(columns) == 8:  # Ensure the line contains the expected number of columns
                try:
                    mc_step = int(columns[0])  # MC_STEP is in the 1st column
                    nmols_1 = float(columns[2])  # Nmols_1 is in the 3rd column
                    pressure = float(columns[4])  # Pressure is in the 5th column
                    mc_steps.append(mc_step)
                    nmols_1_values.append(nmols_1)
                    pressure_values.append(pressure)
                except ValueError:
                    # Ignore lines where conversion to float or int fails
                    pass

    # Calculate the averages
    avg_nmols_1 = sum(nmols_1_values) / len(nmols_1_values) if nmols_1_values else None
    avg_pressure = sum(pressure_values) / len(pressure_values) if pressure_values else None

    # Plot Pressure vs MC_STEP
    plt.figure(figsize=(10, 6))
    plt.plot(mc_steps, pressure_values, label='Pressure', color='b', marker='o')
    plt.xlabel('MC_STEP')
    plt.ylabel('Pressure (bar)')
    plt.title('Pressure vs MC_STEP')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig(output_image_path)

    return avg_nmols_1, avg_pressure

# Usage example
file_path = 'propane_SBA15_32.out.prp'  # Replace with the actual file path
output_image_path = 'pressure_vs_mc_step.png'  # Replace with desired output file path
avg_nmols_1, avg_pressure = calculate_averages_and_save_plot(file_path, output_image_path)
print(f"Average Nmols_1: {avg_nmols_1}")
print(f"Average Pressure: {avg_pressure}")
print(f"Plot saved as {output_image_path}")

