import os
import pandas as pd

# csv path (converted to relative path)
file_path_pypoll = "Pypoll/Resources/election_data.csv"

# read csv
pypoll_data = pd.read_csv(file_path_pypoll)

# total votes
total_votes = len(pypoll_data)

# votes per candidate
candidate_votes = pypoll_data["Candidate"].value_counts()

# find winner
winner = candidate_votes.idxmax()

# results
results = f"""Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
"""
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
results += f"----------------------------\nWinner: {winner}\n----------------------------"

# print results
print(results)

# path to save results
output_folder_path = "Pypoll/Analysis"

# Output file path (constructed using the relative output_folder_path)
output_file_path = os.path.join(output_folder_path, "pypoll_results.txt")

# write results to text file
with open(output_file_path, "w") as output_file:
    output_file.write(results)