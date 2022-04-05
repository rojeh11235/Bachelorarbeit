import re
import time

import src.encryption.rot_random as rot_random
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
        position = [value.start(), value.end()]
        Values_positions.append(position)
    return Values_positions


def protect_tag(message, tag, group_str, group_num, key):
    for value in get_tag_values(message, tag):
        for element in value:
            if element != '':
                message = message.replace(element, rot_random.rot_random(element, group_str, group_num, key))
    return message


def protect_tag_with_positions(message, tag, group_str, group_num, key):
    for position in get_tag_values_positions(message, tag):
        for i in range(position[0], position[1]):
            message = message[:i] + rot_random.rot_random(message[i],group_str, group_num, key) + message[i + 1:]
    return message

def return_tag_with_positions(message, tag, group_str, group_num, key):
    for position in get_tag_values_positions(message, tag):
        for i in range(position[0], position[1]):
            message = message[:i] + rot_random.de_rot_random(message[i],group_str, group_num, key) + message[i + 1:]
    return message


def protect_mt_file(path,output_path, tags, group_str, group_num, key):
    message = open(path).read()
    protected_file = open(
        '{}/protected_mt_file_{}_{}.mt'.format(output_path,get_message_type(message),
                                                                                             time.strftime(
                                                                                                 "%Y%m%d-%H%M%S")),
        'w', )
    for tag in tags:
        if is_tag_exist(message, tag):
            message = protect_tag_with_positions(message, tag, group_str, group_num, key)
    protected_file.write(message)

def return_mt_file(path,output_path, tags, group_str, group_num, key):
    message = open(path).read()
    protected_file = open(
        '{}output/mt_file_{}_{}.mt'.format(output_path,get_message_type(message),
                                                            time.strftime(
                                                                "%Y%m%d-%H%M%S")),
        'w', )
    for tag in tags:
        if is_tag_exist(message, tag):
            message = return_tag_with_positions(message, tag, group_str, group_num, key)
    protected_file.write(message)

#g1=rot_random.random_str_group(False);
#g2=rot_random.random_numeric_group()
#protect_mt_file('../../../data//mt.mt', [59],g1,g2, 123 )

#g1= open('../../../output/random_str_group.txt').read()
#g2= open('../../../output/random_numeric_group.txt').read()
#return_mt_file('../../../output/protected_mt_file_103_20220325-181503.mt', [59],g1,g2, 123 )