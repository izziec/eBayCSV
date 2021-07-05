# import lib
import csv
import sys
# open csv
with open(str(sys.argv[1]), newline='') as csvfile:
    #print('hello')
    # read in csv
    reader = csv.DictReader(csvfile)
    # skip empty row
    next(reader)
    # loop rows
    for row in reader:
        if row['Buyer Name'] != "":
            print(row['Buyer Name']) 
            print(row['Ship To Address 1'])
            if row['Ship To Address 2'] != "":
                print(row['Ship To Address 2'])
            print(row['Buyer City'], row['Buyer State'], row['Buyer Zip'])
        if row['Custom Label'] != "": 
            print(row['Quantity'], "x", row['Custom Label']) 
            print()
