import csv

rows=[]
with open("states.csv") as df:
  csv_read=csv.reader(df)
  fields=next(csv_read)
  for row in csv_read:
    rows.append(row)

state_list=[]
state_dict={}
for element in rows:
  state_list.append(element[5])
for state in state_list:
  state_dict[state]=state_list.count(state)

sorted_dict=sorted(state_dict.items(),key=lambda x:x[1])
sorted_list=reversed(sorted_dict)
temp_list=[]
state_list=[]
for elem in sorted_list:
  temp_list.append(elem)
  
for i in range(len(temp_list)):
  state_list.append(temp_list[i][0])
for state in state_list:
  for element in rows:
    if element[5]==state:
      print(element)