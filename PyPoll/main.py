#Create file paths across operating systems
import os

#Insert module for reading CSV files
import csv

csvfile = os.path.join('..', 'Resources', 'election_data.csv')

#Confirm CSV file pathway
with open('C:/Users/Dell/Downloads/GITHUB/Python-Challenge/Python-Challenge/PyPoll/Resources/election_data.csv') as csvfile:

    # Confirm delimiter and the variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the contents of the CSV file
    print(csvreader)

    # Read the header row
    csv_header = next(csvreader)
    print (f"CSV Header: {csv_header}")

    # To calculate the total number of votes cast
    total_votes = 0 

    #Candidate name and vote count dictionary
    candidate_list_votes = {}
    

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        candidate_name = row[2] 
        total_votes +=1  # total_months = total_months + 1
        if candidate_name  not in candidate_list_votes.keys():
            candidate_list_votes[candidate_name] = 1
        else:
            candidate_list_votes[candidate_name] += 1
        
    print(candidate_list_votes)
        

        #To calculate the percentage of votes each candidate won
        

        #The total number of votes each candidate won
        

        #The winner of the election based on popular vote
        

      


