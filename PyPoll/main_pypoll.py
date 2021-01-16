#create file path
import os
#module for read csv files
import csv

csvpath = os.path.join("..", "resources", "election_data.csv")

#defining variables
candidates = [] 
list_candidates = []
votes_candidate = []
winner_list = []

votes_first = 0
votes_second = 0
votes_third = 0
votes_fourth = 0

#reading the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    #print(f"CSV Header: {csvheader}") checkpoint
    #for row in csvreader: checkpoint
    #   print(row)

    
    for row in csvreader:
        #creating a list for count of votes
        candidates.append(row[2])
         
        candidate = row[2]

        if candidate not in list_candidates:
            #creating a list for candidates, only one per candidate
            list_candidates.append(candidate)

    #counting votes por candidate
    for candidate in candidates:
        if candidate == list_candidates[0]: 
                votes_first += 1
                
        elif candidate == list_candidates[1]:  
                votes_second += 1
                
        elif candidate == list_candidates[2]:
                votes_third += 1
                
        elif candidate == list_candidates[3]:
                votes_fourth += 1
                
    #calculating the winner
    winner_list.append(votes_first)
    winner_list.append(votes_second)
    winner_list.append(votes_third)
    winner_list.append(votes_fourth)
    winner_position = winner_list.index(int(max(winner_list)))
    winner= list_candidates[winner_position]
                         
    #printing in terminal
    print(f"Total Votes: {len(candidates)}") 
    print(list_candidates[0], round(votes_first/len(candidates)*100,3), "%", "(", votes_first, ")")
    print(list_candidates[1], round(votes_second/len(candidates)*100,3), "%", "(", votes_second, ")")
    print(list_candidates[2], round(votes_third/len(candidates)*100,3), "%", "(", votes_third, ")")
    print(list_candidates[3], round(votes_fourth/len(candidates)*100,3), "%", "(", votes_fourth, ")")
    print("Winner: ", winner)

    #generating the output file 
    output_path = os.path.join("..", "resources", "analysis.txt")

    with open('election_results.txt', 'w') as text:
        text.write("Election Results"+ "\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Votes: " + str(len(candidates)) + "\n")
        text.write("----------------------------------------------------------\n")
        text.write(list_candidates[0] + " : " + str(round(votes_first/len(candidates)*100,3)) + "%  (" + str(votes_first) + ")\n")
        text.write(list_candidates[1] + " : " + str(round(votes_second/len(candidates)*100,3)) + "%  (" + str(votes_second) + ")\n")
        text.write(list_candidates[2] + " : " + str(round(votes_third/len(candidates)*100,3)) + "%  (" + str(votes_third) + ")\n")
        text.write(list_candidates[3] + " : " + str(round(votes_fourth/len(candidates)*100,3)) + "%  (" + str(votes_fourth) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + winner + "\n")

       





    #print(f"Total Votes: {len(candidates)}")
    #print(candidates)
    #print(list_candidates)
    #print(votes_candidate)
    #print(candidates[0])
    #print(votes_first)
    #print(votes_second)
    #print(votes_third)
    #print(votes_fourth)
    