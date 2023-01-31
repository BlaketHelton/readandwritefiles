import csv

# open file
with open('EmployeePay.csv', 'r') as input_csv:
    
    # create reader object
    reader = csv.reader(input_csv)
    
    # loop over each row in file
    for row in reader:
        # print out employee details
        print('ID:', row[0])
        print('First Name:', row[1])
        print('Last Name:', row[2])
        print('Salary:', row[3])
        print('Bonus:', row[4])
        print('\n')