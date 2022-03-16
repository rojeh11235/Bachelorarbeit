import time

from src.file.SEPA import SEPA


def protect_name(document, nameSpace):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}MsgRcspt".format(nameSpace)):
            for name in InitgPty.findall("{}Nm".format(nameSpace)):
                name.text = 'xxxxxxx'


def protect_adresse(document, nameSpace):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}InitgPty".format(nameSpace)):
            for PstlAdr in InitgPty.iter("{}PstlAdr".format(nameSpace)):
                 for adressLine in PstlAdr.findall("{}AdrLine".format(nameSpace)):
                         adressLine.text = "xxxxxx"

def protect_GrpHdr(document):
    namespace = SEPA.getNamespace(document.getroot())
    protect_name(document, namespace)
    protect_adresse(document, namespace)
