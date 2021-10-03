from database import DB
import csv
import time

myDB = DB()
myDB.DropTable("accidents")
myDB.CreateAccidentTable()

start_time = time.time()

def convert_to_string(inp):
    return '"' + str(inp) + '"'

with open('db/US_accident_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    formatted_input = ""
    for row in reader:
        if i == 0:
            i += 1
            continue
        row[2] = convert_to_string(row[2])
        for j in range(9, 17):
            row[j] = convert_to_string(row[j])
        filtered_result = row[1:3] + row[4:12] + row[13:14] + row[15:17]
        formatted_input += '(' + ','.join(filtered_result) + '), '
    # print(formatted_input)
    myDB.InsertAccidents(formatted_input[:-2])

print(time.time()-start_time)