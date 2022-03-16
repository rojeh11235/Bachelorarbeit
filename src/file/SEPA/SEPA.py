import re
import time

import src.file.SEPA.camt.GrpHdr as camtg
import src.file.SEPA.camt.Stmt as camtc
import src.file.SEPA.pain.GrpHdr as paing
import src.file.SEPA.pain.PmtInf as painp


def getNamespace(element):
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''


def is_sepa_format(document):
    return getNamespace(document.getroot()).__contains__('urn:iso:std:iso:20022:tech:xsd:')


def get_Sepa_massage_format(document):
    namespace = getNamespace(document.getroot())
    pat = '(?<=xsd:)(.*)(?=})'
    return re.search(pat, namespace).group(0)


def get_Sepa_massage_format1(document):
    namespace = getNamespace(document.getroot())
    if namespace.__contains__('camt'):
        return 'camt'
    elif namespace.__contains__('pain'):
        return 'pain'
    else:
        return 'this Format is not supported'


def protect_sepa(document):
    format = get_Sepa_massage_format1(document)
    if format == 'pain':
        paing.protect_GrpHdr(document)
        painp.protect_PmtInf(document)
        document.write(
            '../output/protected_{}_{}.xml'.format(get_Sepa_massage_format(document), time.strftime("%Y%m%d-%H%M%S")))
    elif format == 'camt':
        camtg.protect_GrpHdr(document)
        camtc.protect_stmt(document)
        document.write(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_{}_{}.xml'.format(get_Sepa_massage_format(document), time.strftime("%Y%m%d-%H%M%S")))
