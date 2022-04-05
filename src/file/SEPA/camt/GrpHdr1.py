import time
from src.encryption import rot_random

from src.file.SEPA import SEPA

def protect_name(document, nameSpace, group_str, _group_num, key):
    for GrpHdr in document.iter("{}GrpHdr".format(nameSpace)):
        for InitgPty in GrpHdr.iter("{}MsgRcspt".format(nameSpace)):
            for name in InitgPty.findall("{}Nm".format(nameSpace)):
                name.text = rot_random.de_rot_random(name.text, group_str, _group_num, key)



def protect_adresse(document, namespace, group_str, _group_num, key):
    for GrpHdr in document.iter("{}GrpHdr".format(namespace)):
        for MsgRcspt in GrpHdr.findall("{}MsgRcspt".format(namespace)):
            for PstlAdr in MsgRcspt.findall("{}PstlAdr".format(namespace)):
                for adressLine in PstlAdr.findall("{}AdrLine".format(namespace)):
                    adressLine.text = rot_random.de_rot_random(adressLine.text, group_str, _group_num, key)


def protect_GrpHdr(document, group_str, _group_num, key):
    namespace = SEPA.getNamespace(document.getroot())
    protect_name(document, namespace, group_str, _group_num, key)
    protect_adresse(document, namespace, group_str, _group_num, key)
