import time

from src.file.SEPA import SEPA


def protect_name(document, nameSpace):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}InitgPty".format(nameSpace)):
            for name in InitgPty.findall("{}Nm".format(nameSpace)):
                name.text = 'Protected_Name'


def protect_adresse(document, nameSpace):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}InitgPty".format(nameSpace)):
            for PstlAdr in InitgPty.findall("{}PstlAdr".format(nameSpace)):
                for AdrLine in PstlAdr.findall("{}AdrLine".format(nameSpace)):
                    AdrLine.text = "Protected_Adresse"

def protect_GrpHdr(document):
    namespace = SEPA.getNamespace(document.getroot())
    protect_name(document, namespace)
    protect_adresse(document, namespace)
