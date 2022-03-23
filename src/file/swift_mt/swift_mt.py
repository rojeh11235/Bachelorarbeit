import re
import time

import src.encryption.rot_47 as rot_47
from src.file.swift_mt import aplication_header
from src.file.swift_mt import data_block
from src.file.swift_mt import pattern


def is_mt_format(message):
    return bool(re.match(pattern.basic_header_pat, message))


def is_tag_exist(message, tag):
    return bool(len(re.findall(r":" + str(tag) + ":", message)) != 0)


def get_message_type(message):
    application_header = aplication_header.get_application_header(message)
    return application_header[4:7]


def get_tag_value(message, tag):
    datablock = data_block.get_data_block(message)
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    return re.search(pat, datablock).group(0).split('\n')


def get_tag_values(message, tag):
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    values = []
    for value in re.finditer(pat, message):
        values.append(value.group(0).split('\n'))
    return values

def get_tag_values_positions(message, tag):
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    Values_positions = []
    for value in re.finditer(pat, message):
        position =[value.start(),value.end()]
        Values_positions.append(position)
    return Values_positions


def protect_tag(message, tag):
    for value in get_tag_values(message, tag):
        for element in value:
            if element != '':
                message = message.replace(element, rot_47.rot47(element))
    return message


def protect_tag_with_positions(message, tag):
    for position in get_tag_values_positions(message, tag):
        for i in range(position[0],position[1]):
            message = message[:i] + rot_47.rot47(message[i]) + message[i + 1:]
    return message



def protect_mt_file(path, tags):
    message = open(path).read()
    protected_file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_mt_file_{}_{}.mt'.format(get_message_type(message),
                                                                                             time.strftime(
                                                                                                 "%Y%m%d-%H%M%S")),
        'w', )
    for tag in tags:
        if is_tag_exist(message, tag):
            message = protect_tag_with_positions(message, tag)
    protected_file.write(message)

