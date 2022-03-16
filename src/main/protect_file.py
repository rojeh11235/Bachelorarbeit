import xml.etree.ElementTree as ET

import src.file.SEPA as sepa
import src.file.SEPA.SEPA as sepa
import src.file.format_check as fs


def protect_file(file_path):
    file_format = fs.get_file_format(file_path)
    if file_format == 'xml':
        document = ET.parse(file_path)
        if sepa.is_sepa_format(document):
            if sepa.get_Sepa_massage_format1(document) == 'camt':
                sepa.protect_sepa(document)


