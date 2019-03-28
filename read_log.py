import sys

def pretty_print_customers(customer_totals):
    for each_customer in customer_totals:
        print(each_customer + " : " + str(customer_totals[each_customer]) + " bytes")

def parse_filename():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please provide a filename.")
        sys.exit(1)    
    return filename

def parse_logfile(logfile):
    customer_download_dict = {}
    customer_id = None
    for line in logfile:
        # Get the customer_id if it exists in the line
        if "CustomerId:" in line:
            after_customerid = line.partition('CustomerId:')[2]
            customer_id = after_customerid.split()[0]
            # Avoid setting customer_id to None
            continue
        # Lets find the bytes:  
        elif customer_id is not None:
            after_customerid = line.partition('Size:')[2]
            bytes = int(after_customerid.split()[0])

          
            if customer_id in customer_download_dict:
                customer_download_dict[customer_id] += bytes
            else:
                customer_download_dict[customer_id] = bytes

        customer_id = None
    return customer_download_dict


def main():
    filename = parse_filename()
    try:
        print(filename)
        with open(filename, "r") as logfile:
            logfile_dict = parse_logfile(logfile)
            pretty_print_customers(logfile_dict)
    except FileNotFoundError:
        print("Could not access file!")
        sys.exit(255)    


if __name__ == "__main__":
    main()
