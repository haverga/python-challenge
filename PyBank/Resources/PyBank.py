import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Variables to store financial analysis results
total_months = 0
net_profit_loss = 0
changes_in_profit_loss = []
previous_month_profit_loss = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

with open(budget_csv, "r", encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skipping the header
    header = next(csvreader)
    
    for row in csvreader:
        # Data from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Total number of months
        total_months += 1

        # Net total amount of "Profit/Losses"
        net_profit_loss += profit_loss

        # Change in profit/loss since the last month
        if total_months > 1:
            change = profit_loss - previous_month_profit_loss
            changes_in_profit_loss.append(change)

            # Greatest increase and decrease in profits
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = date
            elif change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = date
        
        # Previous month's profit/loss for the next iteration
        previous_month_profit_loss = profit_loss

# Average change in profit/loss over the entire period
average_change = sum(changes_in_profit_loss) / len(changes_in_profit_loss)

# Financial analysis results
financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit_loss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})
"""

# Printing the financial analysis results
print(financial_analysis)

# Saving the results to a text file
with open("financial_analysis.txt", "w") as output_file:
    output_file.write(financial_analysis)
