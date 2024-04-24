def main():

    cust_data = open("customer_data_file.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    print(cust_in)

main()