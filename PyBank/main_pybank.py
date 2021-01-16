#This script was created by Carlos Valverde in january 11th and 12th of 2021.

#create file path
import os
#module for read csv files
import csv

csvpath = os.path.join("..", "resources", "budget_data.csv")

#defining variables
months_num = []
amount = []
changes = []

#reading the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    csvheader = next(csvreader)
    #print(f"CSV Header: {csvheader}") checkpoint

    #for row in csvreader: checkpoint
     #   print(row)

    for row in csvreader:
        #Total number of months included in the dataset and total of profit and loses 
        months_num.append(row[0])
        amount.append(int(row[1]))
        
        #To calculate the average of the all changes month by month and the max and min of that changes
    for i in range(1, len(amount)):
        changes.append(amount[i] - amount[i-1])
        Average_Change = sum(changes) / len(changes)

        greatest_increase = max(changes)
        #locating the date of the max change
        date_greatest = str(months_num[changes.index(greatest_increase)+1])

        greatest_decrease = min(changes)
        #locating the date of the min change
        date_decrease = str(months_num[changes.index(greatest_decrease)+1])

#printing in terminal
    print(f"Total Months: {len(months_num)}") 
    print("Total: $", sum(amount))
    print("Average Change: $", round(Average_Change, 2))
    print("Greatest Increase in Profits: ", date_greatest, "($", greatest_increase, ")")
    print("Greatest Decrease in Profits: ", date_decrease, "($", greatest_decrease, ")")

#generating the output file 
    output_path = os.path.join("..", "resources", "analysis.txt")

    with open('financial_analysis.txt', 'w') as text:
        text.write("    Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(len(months_num)) + "\n")
        text.write("    Total: " + "$" + str(sum(amount)) +"\n")
        text.write("    Average Change: " + '$' + str(round(Average_Change, 2)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(date_greatest) + " ($" + str(greatest_increase) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(greatest_decrease) + ")\n")
         

    
  

     
    




