import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile)

searchname = input("Please enter the name to search for: ")
foundflag = False

next(csvfile) #skip the first line that is the header

for record in csvfile: 
    if record[1].lower() == searchname.lower():
        print('match found')
        print()
        print(f"First Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"City: {record[3]}")
        print(f"Country: {record[4]}")
        print(f"Phone: {record[5]}")
        foundflag = True

if not foundflag:
    print('match not found')
