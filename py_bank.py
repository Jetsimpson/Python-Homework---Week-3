import csv 
import os 
total_month = 0
total_net = 0
month_of_change = []
net_change_list= []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


file_to_load = os.path.join("Resources", "budget_data.csv")
with open (file_to_load) as data:
    reader= csv.reader(data)
    header= next (reader)
    first_row = next (reader)
    total_month= total_month+1
    total_net=total_net+ int (first_row[1])
    prev_net = int(first_row[1])
  

    for row in reader: 
        print(row)
        total_month= total_month+1
        total_net=total_net+ int (row[1])
        # net change 
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
net_avg=sum(net_change_list) / len(net_change_list)
print(total_month)
print(total_net)
print(net_avg)
print(greatest_increase[0],greatest_increase[1])
print(greatest_decrease[0],greatest_decrease[1])
