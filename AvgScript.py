import csv
 
# csv file name
filename = "pacific2.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
for field in fields[:10]:
    print("%11s"%field,end=" ")
print('\n')
 
# printing first 5 rows
# print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row[:10]:
        print("%10s"%col,end=" "),
    print('\n')

for row in rows:
    column = []
    for col in row:
        column.append(col)
    row = column

id = ""
index = 0
count = 0
names = []
years = []
counts = []
winds = []
pressures = []
for row in rows:
    if (id != "" and id != row[0]):
        counts.append(count)
        index += 1
        count = 0
    if (count == 0):
        names.append(row[1])
        years.append(row[2][:4])
        winds.append(float(row[8]))
        pressures.append(float(row[9]))
        count += 1
        id = row[0]
    else:
        winds[index] += float(row[8])
        pressures[index] += float(row[9])
        count += 1
        id = row[0]

print(len(counts))

windAvg = 0
pressureAvg = 0
indexTwo = 0
for cnt in counts:
    winds[indexTwo] = winds[indexTwo] / cnt
    pressures[indexTwo] = pressures[indexTwo] / cnt
    indexTwo += 1

outRows = []

indexThree = 0
for name in names:
    #print(name + " " + years[indexThree] + " " + str(winds[indexThree]) + " " + str(pressures[indexThree] if pressures[indexThree] != -999 else 0))
    outRows.append([name, years[indexThree], winds[indexThree], pressures[indexThree]])
    indexThree += 1


outFields = ["NAMES", "YEARS", "WINDSPEED", "PRESSURE"]

with open("new_pacific2.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(outFields)
     
    # writing the data rows
    csvwriter.writerows(outRows)
