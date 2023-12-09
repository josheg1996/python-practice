import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
file_path = '/Users/joshgreen/Downloads/practice.xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path)

# Extract X and Y columns
x_data = df['X']
y_data = df['Y']

# Plot the data
plt.plot(x_data, y_data, marker='o', linestyle='-')  # You can customize the plot style

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Data from Excel File')

# Display the plot
plt.show()