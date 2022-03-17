import re
import time
import src.encryption.scytale as rot47
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
    datablock = data_block.get_data_block(massage)
    pat = "(?<=(:" + str(tag) + ":))((.|\n)*?)(?=\:)"
    values = []
    for value in re.finditer(pat, datablock):
        values.append(value.group(0).split('\n'))
    return values


def protect_tag(massage, tag):
    for value in get_tag_values(massage, tag):
        for element in value:
            if element != '':
                massage = massage.replace(element, rot47.rot47(element))
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
            massage = protect_tag(massage, tag)
    protected_file.write(massage)



