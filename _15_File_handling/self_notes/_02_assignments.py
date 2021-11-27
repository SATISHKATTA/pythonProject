# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output
            
for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json
"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json

"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json

"""import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]"""

# write the program and fetch data using http get and point out number of holidays in england
# &walesthen group them based on year

"""from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))

for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'] )

"""
"""
import requests
from datetime import datetime
data = requests.get("https://www.gov.uk/bank-holidays.json")
dict1 = (data.json())

#seperate england-and-wales data
data1 = dict1['england-and-wales']

#seperate events data
data2 = data1['events']
#print(data2[0]['date'])

dict1 = {}
#create dictionary by making date at key
for i in range(len(data2)):
    dict1[data2[i]['date']] = data2[i]


#sorting based on date
def func(n): 
    return datetime.strptime(n, '%Y-%m-%d').date()

dict2 = sorted(dict1.keys(), key = func)
#print(dict2)

#seperate the year and use sets to avoid duplicates
dates_set = set()
for i in dict2:
    dates_set.add(i[0 : 4])
#print(dates_set)

#sort the years in ascending order
dates_list = sorted(list(dates_set))
print(dates_list)

#create a dictionary with year as key and year count as value
count_dict = {}

for i in dates_list:
    count = 0
    for key in dict1:
        if key.startswith(i):
            count = count + 1
            count_dict[i] = count
#print(count_dict)

#dispalay the final output

for i in dates_list:
    print('\n------------------------', i,' has', count_dict[i], ' holidays------------------------ \n')
    for key in dict1:
        if key.startswith(i):
            print(key, dict1[key])
  """
"""write the program and fetch data using http get and point out number of holidays in england
&walesthen group them based on year"""

# Export the json data into csv file by using url
import json

"""
import csv
with open("https://www.gov.uk/bank-holidays.json") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["result"]
    """


"""
import json
import pandas as pd
df = pd.read_json("https://www.gov.uk/bank-holidays.json")
f = open('satish.csv', 'w')
df.to_csv('satish.csv')
"""

"""
dave = [180]
owen = [50]
amr = [150]
laura = [360]
vic = [0]

dave.append(dave[-1] - 180)
laura.append(laura[-1] + 180/3)
owen.append(owen[-1] + 180/3)
vic.append(vic[-1] + 180/3)

owen.append(owen[-1] - 50)
dave.append(dave[-1] + 50)

amr.append(amr[-1] - 150)
vic.append(vic[-1] + 150/2)
owen.append(owen[-1] + 150/2)

laura.append(laura[-1] - 360)
amr.append(amr[-1]+ 360/2)
vic.append(vic[-1] + 360/2)

print(f"Dave {dave[-1]}, Laura {int(laura[-1])}, Owen {int(owen[-1])}, Vic {int(vic[-1])}, Amr {int(amr[-1])}")

"""

# create user with name,empid, total salary --->user input
# total salary  contains basic, HRA,special allowance,tax--->variable each month
# net salary = basic + HRA+ special-tax --->tax
# expenditure name & amount -user iput ---> variable each month
# net salary -expenditure = total savings
# -ve value -loser +ve value -winner

name = input("Enter the name :")
employee_id = int(input("Enter the employeeid :"))
total_salary = int(input("Enter the  Total salary :"))










