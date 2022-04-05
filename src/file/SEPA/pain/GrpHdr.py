from src.file.SEPA import SEPA
from src.encryption import rot_random


def protect_name(document, namespace, group_str, _group_num, key):
    for GrpHdr in document.iter("{}GrpHdr".format(namespace)):
        for InitgPty in GrpHdr.iter("{}InitgPty".format(namespace)):
            for name in InitgPty.findall("{}Nm".format(namespace)):
                name.text = rot_random.rot_random(name.text,group_str, _group_num, key)


def protect_adresse(document, nameSpace, group_str, _group_num, key):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}InitgPty".format(nameSpace)):
            for PstlAdr in InitgPty.findall("{}PstlAdr".format(nameSpace)):
                for AdrLine in PstlAdr.findall("{}AdrLine".format(nameSpace)):
                    AdrLine.text = rot_random.rot_random( AdrLine.text,group_str, _group_num, key)


def protect_GrpHdr(document, group_str, _group_num, key):
    namespace = SEPA.getNamespace(document.getroot())
    protect_name(document, namespace, group_str, _group_num, key)
    protect_adresse(document, namespace, group_str, _group_num, key)



