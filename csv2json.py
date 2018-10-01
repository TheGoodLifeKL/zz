import json 
import sys
import csv
def csv2json(file_path):
    fcsv = csv.reader(open(file_path,'r'))
    for line in fcsv:
        if line[0] is not ",":
            di1 = dict()
            di1[line[0]] = [x for x in line[1:]] 
            for key,value in di1.items():
                if value[0] is not ",":
                    di2 = {}
                    di2[di1[key][0]] = value[1:-1]
                    print(di2)
            print(di1)

                   
                # if di1[line[0]][0] is not ",":
                #     di2 = {}
                #     di2[di1[line[0]][0]] = [y for y in di1[line[0]][1:-1]]
                #     print(di2)
csv2json("/home/python/Desktop/history.csv")



