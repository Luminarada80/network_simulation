import pandas as pd
import matplotlib.pyplot as plt

# Data from the provided table
data = {
    "Num Genes": [10, 20, 30, 40, 50, 60, 70, 80, 90],
    "Avg": [99.69, 91.78, 97.13, 98.71, 98.94, 98.07, 98.49, 98.69, 99.02],
    "Stdev": [0.1, 4.77, 1.1, 1.71, 0.44, 1.05, 1.05, 1.12, 0.6],
    "Min": [99.1, 85.2, 94.13, 92.0, 97.04, 94.73, 93.26, 94.8, 96.09],
    "Max": [100.0, 99.8, 99.73, 99.9, 99.84, 99.87, 99.94, 99.95, 99.78]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Prepare the data for box plots
box_plot_data = []
for i in range(len(df)):
    num_genes = df.iloc[i]["Num Genes"]
    avg = df.iloc[i]["Avg"]
    stdev = df.iloc[i]["Stdev"]
    min_val = df.iloc[i]["Min"]
    max_val = df.iloc[i]["Max"]
    
    # Simulate the data for the box plot
    values = [avg - stdev, avg, avg + stdev]
    values = [min(max(val, min_val), max_val) for val in values]  # Ensure values are within min and max
    box_plot_data.append(values)

# Create the box plots with the further increased font size
plt.figure(figsize=(12, 8))
plt.boxplot(box_plot_data, positions=df["Num Genes"], widths=5)
plt.xticks(df["Num Genes"], fontsize=14)
plt.xlabel('Number of Genes', fontsize=18)
plt.ylabel('Accuracy', fontsize=18)
plt.title('scBONITA Rule Recovery Accuracy', fontsize=20)
plt.ylim(0, 100)
plt.grid(True)
plt.show()
