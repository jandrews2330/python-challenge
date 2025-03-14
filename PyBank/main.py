# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:\\Users\\jenn2\\OneDrive\\Documents\\Data Analytics Bootcamp\\Module 3 Challenge\\python-challenge\\PyBank\\Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("C:\\Users\\jenn2\OneDrive\Documents\\Data Analytics Bootcamp\\Module 3 Challenge\\python-challenge\\PyBank\\analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
monthly_changes = []
previous_profit = None
months = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
    

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Store the month (assuming the month is in the first column)
        months.append(row[0])

        # Track the net change
        profit = int(row[1])
        total_net += profit

        # Calculate monthly change
        if previous_profit is not None:
            change = profit - previous_profit
            monthly_changes.append(change)
        
        # Update previous profit for the next iteration
        previous_profit = profit
        
        # Calculate the average net change across the months
        if len(monthly_changes) > 0:
            average_change = sum(monthly_changes)/len(monthly_changes)
        # Calculate the greatest increase in profits (month and amount)
            greatest_increase = max(monthly_changes)
            greatest_decrease = min(monthly_changes)

        # Calculate the greatest decrease in losses (month and amount)
            month_of_greatest_increase = months[monthly_changes.index(greatest_increase) + 1]
            month_of_greatest_decrease = months[monthly_changes.index(greatest_decrease) + 1]

        else:
            average_change = 0
            greatest_increase = 0
            greatest_decrease = 0
            month_of_greatest_increase = None
            month_of_greatest_decrease = None

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: Month {month_of_greatest_increase} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: Month {month_of_greatest_decrease} (${greatest_decrease})\n"
)


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
