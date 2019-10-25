import csv

def create_csv():
    path = "aa.csv"
    with open(path,'a+',newline='') as f:
        csv_write = csv.writer(f)
        data_row = ["1","2"]
        csv_write.writerow(data_row)
        data_row = ["2", "3"]
        csv_write.writerow(data_row)

if __name__ == '__main__':
    create_csv()