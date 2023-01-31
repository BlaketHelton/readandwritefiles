import csv

# read the sales.csv file
with open('sales.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # create a dictionary to store the customer totals
    customer_totals = {}

    # skip the header row
    next(csv_reader)

    # iterate over the rows in the csv
    for row in csv_reader:
        # get the customer id
        customer_id = row[0]
        # get the subtotal, tax amount, and freight
        subtotal = float(row[3])
        tax_amt = float(row[4])
        freight = float(row[5])
        # calculate the total
        total = subtotal + tax_amt + freight

        # add the total to the dictionary
        if customer_id in customer_totals.keys():
            customer_totals[customer_id] += total
        else:
            customer_totals[customer_id] = total

# write the data to a new csv file
with open('salesreport.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # write the header row
    csv_writer.writerow(['CustomerID' ' | ' 'Total'])

    # iterate over the customer data
    for customer_id, total in customer_totals.items():
        # write the customer data
        csv_writer.writerow([customer_id, round(total, 2)])

# close the file
csv_file.close()

