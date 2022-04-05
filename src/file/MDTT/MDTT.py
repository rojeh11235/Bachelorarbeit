import csv
import time

from src.encryption import rot_random

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


def protect_mdtt_file(file_path, output_path, column_to_protect, group_str, _group_num, key):
    rows = make_array_from_csv(file_path)
    file = open(
        '{}/protected_mdtt_{}_{}.csv'.format(output_path, get_MDTT_type(file_path),
                                             time.strftime(
                                                 "%Y%m%d-%H%M%S")), 'w',
        encoding='UTF8', newline='')
    writer = csv.writer(file, delimiter=';')
    for row in rows:
        for column in column_to_protect:
            column = int(column)
            if column in range(len(row) - 1):
                for i in range(len(row[column])):
                    if row[0] in MDTT:
                        row[column] = row[column][:i] + (
                            rot_random.rot_random(row[column][i], group_str, _group_num, key)) + \
                                      row[column][i + 1:]
        writer.writerow(row)


def protect_mdtt_files(file_path, output_path, customer_column_to_protect, user_column_to_protect,
                       account_column_to_protect, group_str, _group_num, key):
    if get_MDTT_type(file_path) == 'Customer':
        protect_mdtt_file(file_path, output_path, customer_column_to_protect, group_str, _group_num, key)
    if get_MDTT_type(file_path) == 'User':
        protect_mdtt_file(file_path, output_path, user_column_to_protect, group_str, _group_num, key)
    if get_MDTT_type(file_path) == 'Account':
        protect_mdtt_file(file_path, output_path, account_column_to_protect, group_str, _group_num, key)


def return_mdtt(file_path, output_path, column_to_protect, group_str, _group_num, key):
    rows = make_array_from_csv(file_path)
    file = open(
        '{}/protected_mdtt_{}_{}.csv'.format(output_path, get_MDTT_type(file_path),
                                             time.strftime(
                                                 "%Y%m%d-%H%M%S")), 'w',
        encoding='UTF8', newline='')
    writer = csv.writer(file, delimiter=';')
    for row in rows:
        for column in column_to_protect:
            column = int(column)
            for i in range(len(row[column])):
                if row[0] in MDTT:
                    row[column] = row[column][:i] + (
                        rot_random.de_rot_random(row[column][i], group_str, _group_num, key)) + \
                                  row[column][i + 1:]
        writer.writerow(row)

# print(make_array_from_csv('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\KONTODATEI.csv')[0][0])
# print(is_MDTT_file('C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\KONTODATEI.csv'))
# g1 = rot_random.random_str_group(False)
# g2 = rot_random.random_numeric_group()
# protect_mdtt('../../../data/KONTODATEI.csv', [1, 3,5],g1,g2,123)
# array = make_array_from_csv('')
# def protect_mdtt(file_path, output_path, costomer_column_to_protect,user_column_to_protect,account_column_to_protect, group_str, _group_num, key):
#     rows = make_array_from_csv(file_path)
#     file = open(
#         '{}/protected_mdtt_{}_{}.csv'.format(output_path, get_MDTT_type(file_path),
#                                              time.strftime(
#                                                  "%Y%m%d-%H%M%S")), 'w',
#         encoding='UTF8', newline='')
#     writer = csv.writer(file, delimiter=';')
#     for row in rows:
#         if get_MDTT_type(file_path) == 'account':
#             for column in account_column_to_protect:
#                 column = int(column)
#                 if column in range(len(row) - 1):
#                     for i in range(len(row[column]) - 1):
#                         if row[0] in MDTT:
#                             row[column] = row[column][:i] + (
#                                 rot_random.rot_random(row[column][i], group_str, _group_num, key)) + \
#                                           row[column][i + 1:]
#             writer.writerow(row)
#             if get_MDTT_type(file_path) == 'user':
#                 for column in user_column_to_protect:
#                     column = int(column)
#                     if column in range(len(row) - 1):
#                         for i in range(len(row[column]) - 1):
#                             if row[0] in MDTT:
#                                 row[column] = row[column][:i] + (
#                                     rot_random.rot_random(row[column][i], group_str, _group_num, key)) + \
#                                               row[column][i + 1:]
#             writer.writerow(row)
#             if get_MDTT_type(file_path) == 'costomer':
#                 for column in costomer_column_to_protect:
#                     column = int(column)
#                     if column in range(len(row) - 1):
#                         for i in range(len(row[column]) - 1):
#                             if row[0] in MDTT:
#                                 row[column] = row[column][:i] + (
#                                     rot_random.rot_random(row[column][i], group_str, _group_num, key)) + \
#                                               row[column][i + 1:]
#             writer.writerow(row)
