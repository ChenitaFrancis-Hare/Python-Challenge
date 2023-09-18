#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate".
#You will be given a set of poll data called election_data.csv.  Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    #1. The total number of votes cast
    #2. A complete list of candidates who received votes
    #3. To calculate the percentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote

#Create file paths across operating systems
import os

#Insert module for reading CSV files
import csv

csvpath = os.path.join('C:/Users/Dell/Downloads/GITHUB/Python-Challenge/Python-Challenge/PyPoll/Resources/election_data.csv')


# Set total votes to 0 for counter
total_votes = 0 


#Create list for candidate name and vote count
candidate_list = []
stockham_votes = 0
degette_votes = 0
doane_votes = 0


#Confirm CSV file pathway
with open(csvpath) as text:

    # Confirm delimiter and the variable that holds contents
    csvreader = csv.reader(text, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)
 
    # Read each row of data after the header
    for row in csvreader:
        total_votes  += 1
        candidate_name = row[2] 

    #Check column for duplicate entry        
    if candidate_name not in candidate_list:
            # Add the item to the candidate_list
            candidate_list.append(candidate_name)

    #2. A complete list of candidates who received votes
    for i in range(len(candidate_name)):
        if candidate_name == candidate_list[0]:
                stockham_votes += 1
        elif candidate_name == candidate_list[1]:
                degette_votes += 1
        elif candidate_name == candidate_list[2]:
                doane_votes += 1

    
   #3. Calculate the percentage of votes for each candidate  
    perc_votes_stockham = (stockham_votes/total_votes)*100
    perc_votes_degette = (degette_votes/total_votes)*100
    perc_votes_doane = (doane_votes/total_votes)*100

        

    #5. The winner of the election based on popular vote
    tally = {"Charles Casper Stockham": (perc_votes_stockham), "Diana Degette": (perc_votes_degette), "Raymon Anthony Doane":(perc_votes_doane)}
    # Find maximum key in the dictionary
    winner =  max(tally, key=tally.get)



# Format and print analysis findings
    print("\n")
    print("Election Results")
    print("\n--------------------------\n")
    print(f"Total Votes:{total_votes}\n")
    print("\n--------------------------\n")
    print(f" Charles Casper Stockham: {perc_votes_stockham:.2f}% ({stockham_votes})\n")
    print(f" Diana DeGette: {perc_votes_degette:.2f}% ({degette_votes})\n")
    print(f" Raymon Anthony Doane: {perc_votes_doane:.2f}% ({doane_votes})\n")
    print("\n--------------------------\n")
    print(f"Winner:{winner}\n")    
    print("\n--------------------------\n")

# # Specify the file to write to
txtfile_output = os.path.join('C:/Users/Dell/Downloads/Gitrepo/Python-Challenge/PyPoll/Resources/election_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(txtfile_output, 'w') as txtfile_output:
    txtfile_output.write("\n")
    txtfile_output.write("Election Results")
    txtfile_output.write("\n--------------------------\n")
    txtfile_output.write(f"Total Votes: {total_votes}\n")
    txtfile_output.write("\n--------------------------\n")
    txtfile_output.write(f" Charles Casper Stockham: {perc_votes_stockham:.2f}% {stockham_votes}\n")
    txtfile_output.write(f" Diana DeGette: {perc_votes_degette:.2f}% {degette_votes}\n")
    txtfile_output.write(f" Raymon Anthony Doane: {perc_votes_doane:.2f}% {doane_votes}\n")
    txtfile_output.write("\n--------------------------\n")
    txtfile_output.write(f"Winner:{winner}\n")    
    txtfile_output.write("\n--------------------------\n")
    txtfile_output.close()
