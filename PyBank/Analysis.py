print("                        ")
print("Financial Analysis")
print("                        ")
print("------------------------")
print("                        ")

import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")

count = 1
profit_loss_list = list()
profit_loss_change = list()
profit_loss_changes = list()
prior_value = list()
next_value = list()
list_of_dates = list()
max_date = ""
min_date = ""

with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    first_row = next(csv_reader)
    prior_value = int(first_row[1])
    profit_loss_list.append(prior_value)

    for row in csv_reader:
        count +=1
        list_of_dates.append(row[0])
        
        profit_loss = int(row[1])
        
        profit_loss_list.append(profit_loss)

        profit_loss_change.append(profit_loss)
        
        next_value = int(row[1])
        change = next_value - prior_value

        profit_loss_changes.append(change)
         
        prior_value = next_value

    max_change = max(profit_loss_changes)
    profit_loss_changes.index(max_change)
    max_change_index = profit_loss_changes.index(max_change)
    max_date = list_of_dates[max_change_index]

    min_change = min(profit_loss_changes)
    profit_loss_changes.index(min_change)
    min_change_index = profit_loss_changes.index(min_change)
    min_date = list_of_dates[min_change_index]

    max_change = max(profit_loss_changes)
    min_change = min(profit_loss_changes)

    t = sum(profit_loss_list)    
    
print(f"Total Months: {count}")
print("                        ")
print(f"Total: ${t}")
print("                        ")
import statistics
print(f"Average Change: ${round(statistics.mean(profit_loss_changes), 2)}")
print("                        ")
print(f"Greatest Increase in Profits: ({max_date}) (${max_change})")
print("                        ")
print(f"Greatest Decrease in Profits: ({min_date})  (${min_change})")
print("                        ")