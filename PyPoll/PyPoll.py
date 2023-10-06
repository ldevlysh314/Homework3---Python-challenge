print("                        ")
print("Election Results")
print("                        ")
print("------------------------")
print("                        ")

import csv
import os
from sqlite3 import Row

csvpath = os.path.join("Resources", "election_data.csv")

count = 0
total_votes = list()
votes_per_candidate = list()
percent_per_candidate = list()
#ccs_candidate = list()
#ddg_candidate = list()
#rad_candidate = list()
#candidates = list()

with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    #candidates = (row[2])
    #string_candidates = ['Charles Casper Stockham', 'Diana GeGette', 'Raymon Anthony Doane']

    #if candidates == ("Charles Casper Stockham")
        #ccs_candidate = candidates.append("Charles Casper Stockham")
    #elif candidates == ("Diana DeGette")
        #ddg_candidate = candidates.append("Diana DeGette")
    #else rad_candidate = candidates.append("Raymon Anthony Doane")

    #ccs_count = candidates.append("Charles Casper Stockham")

    total_votes = len(list(csv_reader))

print (f"Total Votes: {total_votes}")
print ("                        ")
print ("------------------------")
print ("                        ")
print (f"Charles Casper Stockham:")
print ("                        ")
print (f"Diana DeGette:")
print ("                        ")
print (f"Raymon Anthony Doane:")
print ("                        ")