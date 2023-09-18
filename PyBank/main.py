#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Import os module to allow us to create file paths across operating systems
import os

# Import csv module to interact(read/write) with CSV files
import csv

csvpath = os.path.join('C:/Users/Dell/Downloads/Gitrepo/Python-Challenge/PyBank/Resources/budget_data.csv')

# Create empty lists to store data
total_months = []
net_profit = [] 
#Create empty list to store profit change
profit_change = []


# Method 2: Improved Reading using CSV module
# Navigate to CSV directory
with open(csvpath) as csvfile:
  
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1])) 

                 
    # To calculate the average of the "Profit/Losses" changes
    for i in range(len(net_profit)-1):
        profit_change.append(net_profit[i+1]-net_profit[i])
       

        # To calculate the greatest increase in profits (date and amount) over the entire period
        greatest_increase = max(profit_change)
        greatest_month_increase = total_months[profit_change.index(greatest_increase)+1]

        # To calculate the greatest decrease in profits (date and amount) over the entire period
        greatest_decrease = min(profit_change)
        greatest_month_decrease = total_months[profit_change.index(greatest_decrease)+1]

      

# Format and print analysis findings
print("\n")
print("Financial Analysis")
print("\n--------------------------\n")
print(f"Total Months:{len(total_months)}\n")
print(f"Total: ${sum(net_profit)}\n")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change))}\n")
print(f"Greatest Increase in Profits: {greatest_month_increase} (${(str(greatest_increase))})\n")
print(f"Greatest Decrease in Profits: {greatest_month_decrease} (${(str(greatest_decrease))})\n")



# Export analysis results to text file
# # Specify the file to write to
txtfile_output = os.path.join('C:/Users/Dell/Downloads/Gitrepo/Python-Challenge/PyBank/Analysis/financial_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(txtfile_output, 'w') as txtfile_output:
    txtfile_output.write("\n")
    txtfile_output.write("Financial Analysis")
    txtfile_output.write("\n--------------------------\n")
    txtfile_output.write(f"Total Months:{len(total_months)}\n")
    txtfile_output.write(f"Total: ${sum(net_profit)}\n")
    txtfile_output.write(f"Average Change: ${round(sum(profit_change)/len(profit_change))}\n")
    txtfile_output.write(f"Greatest Increase in Profits: {greatest_month_increase} (${(str(greatest_increase))})\n")
    txtfile_output.write(f"Greatest Decrease in Profits: {greatest_month_decrease} (${(str(greatest_decrease))})\n")
    txtfile_output.close()