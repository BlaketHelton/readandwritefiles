import csv

# open input file 
with open('customers.csv', 'r') as input_csv:
    # create reader object
    reader = csv.reader(input_csv)
    
    # open output file
    with open('customer_info.csv', 'w') as output_csv:
        # create writer object
        writer = csv.writer(output_csv)
        
        # loop over each row in input file
        for row in reader:
            # write customer name and country to output file
            writer.writerow([row[1], row[4]])

