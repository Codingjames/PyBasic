import csv


file_name = 'data.csv'

def write_csv(data_list):
    with open(file_name,'w',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(data_list)


def read_csv():
    with open(file_name,'r',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        return list(fr)
    