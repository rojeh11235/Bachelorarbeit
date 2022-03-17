import xml.etree.ElementTree as ET

import src.file.SEPA as sepa
import src.file.dtazv.DTAZV as dtazv
import src.file.MDTT.MDTT as mdtt
import src.file.swift_mt.swift_mt as mt

import src.file.format_check as fs


def protect_file(file_path):
    file_format = fs.get_file_format(file_path)
    if file_format == 'xml':
        document = ET.parse(file_path)
        if sepa.is_sepa_format(document):
            if sepa.get_Sepa_message_format1(document) == 'camt':
                sepa.protect_sepa(document)
    elif file_format == 'txt':
        dtazv.protect_dtazv(file_path)
    elif file_format == 'mt':
        mt.protect_mt_file(file_path, [50])
    elif file_format == 'mdtt':
        mdtt.protect_mdtt(file_path, [4])
    else:
        print("Not supported format")

