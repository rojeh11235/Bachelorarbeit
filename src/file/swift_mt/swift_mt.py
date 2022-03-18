import re
import time

import src.encryption.rot_47 as rot_47
from src.file.swift_mt import aplication_header
from src.file.swift_mt import data_block
from src.file.swift_mt import pattern


def is_mt_format(massage):
    return bool(re.match(pattern.basic_header_pat, massage))


def is_tag_exist(massage, tag):
    return bool(len(re.findall(r":" + str(tag) + ":", massage)) != 0)


def get_message_type(massage):
    application_header = aplication_header.get_application_header(massage)
    return application_header[4:7]


def get_tag_value(massage, tag):
    datablock = data_block.get_data_block(massage)
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    return re.search(pat, datablock).group(0).split('\n')


def get_tag_values(massage, tag):
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    values = []
    for value in re.finditer(pat, massage):
        values.append(value.group(0).split('\n'))
    return values

def get_tag_values_positions(massage, tag):
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    Values_positions = []
    for value in re.finditer(pat, massage):
        position =[value.start(),value.end()]
        Values_positions.append(position)
    return Values_positions


def protect_tag(massage, tag):
    for value in get_tag_values(massage, tag):
        for element in value:
            if element != '':
                massage = massage.replace(element, rot_47.rot47(element))
    return massage


def protect_tag_with_positions(massage, tag):
    for position in get_tag_values_positions(massage, tag):
        for i in range(position[0],position[1]):
            massage = massage[:i] + rot_47.rot47(massage[i]) + massage[i + 1:]
    return massage



def protect_mt_file(path, tags):
    massage = open(path).read()
    protected_file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_mt_file_{}_{}.mt'.format(get_message_type(massage),
                                                                                             time.strftime(
                                                                                                 "%Y%m%d-%H%M%S")),
        'w', )
    for tag in tags:
        if is_tag_exist(massage, tag):
            massage = protect_tag_with_positions(massage, tag)
    protected_file.write(massage)


massage = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\mt.mt").read()
protect_tag_with_positions(massage, 59)
open(
    'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_mt_file_{}_{}.mt'.format(get_message_type(massage),
                                                                                         time.strftime(
                                                                                             "%Y%m%d-%H%M%S")),
    'w', ).write(massage)
protect_mt_file("C:\\NAK\\BachelorArbeit\\Filesprotecter\\data\\mt.mt",[59])