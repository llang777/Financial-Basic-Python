import os
import pandas as pd

# csv path (converted to relative path)
file_path_pybank = "Pybank/Resources/budget_data.csv"

# read csv
pybank_data = pd.read_csv(file_path_pybank)

# number of months
total_months = len(pybank_data)

# amount of profit/losses
net_total = pybank_data["Profit/Losses"].sum()

# change in profit/losses
pybank_data["Change"] = pybank_data["Profit/Losses"].diff()

# average change
average_change = pybank_data["Change"].mean()

# increase and date
greatest_increase = pybank_data.loc[pybank_data["Change"].idxmax()]

# decrease and date
greatest_decrease = pybank_data.loc[pybank_data["Change"].idxmin()]


# path to save results
output_folder_path = "Pybank/Analysis"

# results calculation
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total:.0f}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']:.0f})
Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:.0f})
"""

# print results
print(results)

# file path
output_file_path = os.path.join(output_folder_path, "pybank_results.txt")

# write results to text file
with open(output_file_path, "w") as output_file:
    output_file.write(results)