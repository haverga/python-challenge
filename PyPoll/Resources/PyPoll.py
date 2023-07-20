import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Variables
total_votes = 0
candidates_votes = {}

# Reading CSV file and counting votes
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Percentage of votes for each candidate
candidates_percentages = {}
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    candidates_percentages[candidate] = percentage

winner = max(candidates_votes, key=candidates_votes.get)

# Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Saving results to a text file
output_file = "election_results.txt"
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates_votes.items():
        txtfile.write(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results saved to {output_file}.")