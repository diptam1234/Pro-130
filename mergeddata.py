import csv

data_set_1 = []
data_set_2 = []

with open("bright_stars.csv","r") as f:
    datareader = csv.reader(f)
    for row in datareader:
        data_set_1.append(row)


with open("unit_converted_stars.csv","r") as f:
    datareader = csv.reader(f)      
    for row in datareader:
        data_set_2.append(row)


header_1 = data_set_1[0]       
planet_data_1 = data_set_1[1:] 

header_2 = data_set_2[0]
planet_data_2 = data_set_2[1:]

headers = header_1 + header_2 

planet_data = []

for index , datarow in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+ planet_data_2[index])


with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)   
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)











