import csv
import time
from src.encryption import rot_47

MDTT = ['Account', 'User', 'Customer']


def is_MDTT_file(file_path):
    return (get_MDTT_type(file_path) in MDTT)


def get_MDTT_type(file_path):
    return make_array_from_csv(file_path)[0][0]


def make_array_from_csv(file_path):
    file = open(file_path)
    csv_reader = csv.reader(file)
    rows = []
    for row in csv_reader:
        rows.append(row[0].split(';'))
    return rows


def protect_mdtt(file_path, column_to_protect):
    rows = make_array_from_csv(file_path)
    file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_mdtt_{}_{}.csv'.format(get_MDTT_type(file_path),
                                                                                           time.strftime(
                                                                                               "%Y%m%d-%H%M%S")), 'w',
        encoding='UTF8',newline='')
    writer = csv.writer(file, delimiter=';')
    for row in rows:
        for column in column_to_protect:
            for i in range(len(row[column])-1):
                row[column] = row[column][:i] + (rot_47.rot47(row[column][i])) + row[column][i + 1:]
        writer.writerow(row)

def return_mdtt(file_path, column_to_protect):
    rows = make_array_from_csv(file_path)
    file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_mdtt_{}_{}.csv'.format(get_MDTT_type(file_path),
                                                                                           time.strftime(
                                                                                               "%Y%m%d-%H%M%S")), 'w',
        encoding='UTF8', newline='')
    writer = csv.writer(file, delimiter=';')
    for row in rows:
        for column in column_to_protect:
            for i in range(len(row[column])-1):
                row[column] = row[column][:i] + (rot_47.rot47(row[column][i])) + row[column][i + 1:]
        writer.writerow(row)


#print(make_array_from_csv('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\KONTODATEI.csv')[0][0])
#print(is_MDTT_file('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\KONTODATEI.csv'))
#protect_mdtt('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\protected_mdtt_Account_20220317-212120.csv', [1, 3])
#array = make_array_from_csv('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\KONTODATEI.csv')
