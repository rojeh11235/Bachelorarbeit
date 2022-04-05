import re
import time
import xml.etree.ElementTree as ET
from src.encryption import rot_random
import src.file.SEPA.camt.Stmt as camtc
import src.file.SEPA.pain.GrpHdr as paing
import src.file.SEPA.pain.PmtInf as painp
from src.file.SEPA.camt import GrpHdr


def getNamespace(element):
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''


def is_sepa_format(path):
    document = ET.parse(path)
    return getNamespace(document.getroot()).__contains__('urn:iso:std:iso:20022:tech:xsd:')


def get_Sepa_message_format(document):
    namespace = getNamespace(document.getroot())
    pat = '(?<=xsd:)(.*)(?=})'
    return re.search(pat, namespace).group(0)


def get_Sepa_message_format1(document):
    namespace = getNamespace(document.getroot())
    if namespace.__contains__('camt'):
        return 'camt'
    elif namespace.__contains__('pain'):
        return 'pain'
    else:
        return 'this Format is not supported'


def protect_sepa(path, output_path, group_str, group_num, key):
    document = ET.parse(path)
    formate = get_Sepa_message_format1(document)
    if formate == 'pain':
        paing.protect_GrpHdr(document, group_str, group_num, key)
        painp.protect_PmtInf(document, group_str, group_num, key)
        document.write(
            '{}/protected_{}_{}.xml'.format(output_path, get_Sepa_message_format(document),
                                                   time.strftime("%Y%m%d-%H%M%S")))
    elif formate == 'camt':
        GrpHdr.protect_GrpHdr(document, group_str, group_num, key)
        camtc.protect_stmt(document, group_str, group_num, key)
        document.write(
            '{}/protected_{}_{}.xml'.format(output_path, get_Sepa_message_format(document),
                                                   time.strftime("%Y%m%d-%H%M%S")))

# g1 = rot_random.random_str_group(False)
# g2 = rot_random.random_numeric_group()
# protect_sepa('../../../data/oain1.xml', g1, g2, 12)

# g1= open('../../../output/random_str_group.txt').read()
# g2= open('../../../output/random_numeric_group.txt').read()
# protect_sepa('../../../output/protected_mt_file_103_20220325-181503.mt', [59],g1,g2, 123 )
