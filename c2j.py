
import os 
import csv

file_path = "/home/python/Desktop/history.csv"
with open(file_path,"r") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    header = rows[0]
    for rowOne in rows[1:]:
        json_row = {}
        for i in range(0,len(rowOne)):
            json_row[header[i]] = rowOne[i]
        print(json_row)
