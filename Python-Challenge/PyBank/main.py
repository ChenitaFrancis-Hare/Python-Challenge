#Create file paths across operating systems
import os

#Insert module for reading CSV files
import csv

csvreader = os.path.join('..', 'Resources', 'budget_data.csv')

#Confirm CSV file pathway
with open('budget_data.csv','r') as csvfile:

    # Confirm delimiter and the variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the contents of the CSV file
    print(csvreader)

    # Read the header row
    csv_header = next(csvreader)
    print (f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

         # To calculate the total number of months in the dataset
        total_months = 0
        total_months = [0]

        # To calculate the net total amount of "Profit/Losses" over the entire period
        net_profit = []

         # To calculate the changes in "Profit/Losses" over the entire period
        av_change = []

        for row in csvreader:
            total_month=row[0]
            total_months.append(row[0])
            net_profit=row[1]
            net_profit.append(int(row[1]))
       
        total_months = len
        print(len(total_months))
           
        # To calculate the average of the "Profit/Losses" changes
        for i in range(len(net_profit)-1):
            av_change.append(net_profit[i+1]-net_profit[i])

        # To calculate the greatest increase in profits (date and amount) over the entire period
        increase = max(av_change)
        month_increase = av_change.index(max(av_change))+1
        decrease = min(av_change)
        month_decrease = av_change.index(min(av_change))+1

        # To calculate the greatest decrease in profits (date and amount) over the entire period

# Analysis Findings
print("Financial Analysis")
print("--------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change: {round(sum(av_change)/len(av_change))}")
print(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})")

#Export analysis results to text file
