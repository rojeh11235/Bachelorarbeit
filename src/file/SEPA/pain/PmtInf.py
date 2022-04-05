from src.encryption import rot_random
from src.file.SEPA import SEPA


def protect_debitor(document, namespace, group_str, _group_num, key):
    for pmttpinf in get_pmtinf(document, namespace):
        for dbtr in pmttpinf.findall("{}Dbtr".format(namespace)):
            protect_postal_adresse(dbtr, namespace, group_str, _group_num, key)
            for name in dbtr.findall("{}Nm".format(namespace)):
                name.text = rot_random.de_rot_random(name.text, group_str, _group_num, key)
        protect_account(pmttpinf, "DbtrAcct", namespace, group_str, _group_num, key)


def protect_creditor(document, namespace, group_str, _group_num, key):
    for pmttpinf in get_pmtinf(document, namespace):
        for cdttrftxinf in pmttpinf.findall("{}CdtTrfTxInf".format(namespace)):
            for Cdtr in cdttrftxinf.findall("{}Cdtr".format(namespace)):
                protect_postal_adresse(Cdtr, namespace, group_str, _group_num, key)
                for name in Cdtr.findall("{}Nm".format(namespace)):
                    name.text = rot_random.de_rot_random(name.text, group_str, _group_num, key)
            protect_account(cdttrftxinf, "CdtrAcct", namespace, group_str, _group_num, key)


def protect_postal_adresse(adresse_owner, namespace, group_str, _group_num, key):
    for pstladr in adresse_owner.findall("{}PstlAdr".format(namespace, )):
        for adrline in pstladr.findall("{}AdrLine".format(namespace)):
            adrline.text = rot_random.rot_random(adrline.text, group_str, _group_num, key)


def protect_account(_stmt, _account, namespace, group_str, _group_num, key):
    for acc in _stmt.iter("{}{}".format(namespace, _account)):
        for account_name in acc.findall("{}Nm".format(namespace)):
            account_name.text = rot_random.de_rot_random(account_name.text, group_str, _group_num, key)
        for account_owner in acc.findall("{}Ownr".format(namespace)):
            for owner_name in account_owner.findall("{}Nm".format(namespace)):
                owner_name.text = rot_random.de_rot_random(owner_name.text, group_str, _group_num, key)
            protect_postal_adresse(account_owner, namespace)
        for id in acc.findall("{}Id".format(namespace)):
            for iban in id.findall("{}IBAN".format(namespace)):
                iban.text = rot_random.rot_random(iban.text, group_str, _group_num, key)


def protect_ultimate_debitor(document, namespace, group_str, _group_num, key):
    for CdtTrfTxInf in get_cdttrftxinf(document, namespace):
        for UltmtDbtr in CdtTrfTxInf.findall("{}UltmtDbtr".format(namespace)):
            protect_postal_adresse(UltmtDbtr, namespace, group_str, _group_num, key)
            for name in UltmtDbtr.findall("{}Nm".format(namespace)):
                name.text = rot_random.rot_random(name.text, group_str, _group_num, key)
        protect_account(CdtTrfTxInf, "UltmtDbtrAcc", namespace, group_str, _group_num, key)


def protect_ultimate_creditor(document, namespace, group_str, _group_num, key):
    for CdtTrfTxInf in get_cdttrftxinf(document, namespace):
        for UltmtCdtr in CdtTrfTxInf.findall("{}UltmtCdtr".format(namespace)):
            protect_postal_adresse(UltmtCdtr, namespace, group_str, _group_num, key)
            for name in UltmtCdtr.findall("{}Nm".format(namespace, group_str, _group_num, key)):
                name.text = rot_random.rot_random(name.text, group_str, _group_num, key)
        protect_account(CdtTrfTxInf, "UltmtDbtrAcc", namespace, group_str, _group_num, key)


def get_pmtinf(document, namespace):
    for CstmrCdtTrfInitn in document.findall("{}CstmrCdtTrfInitn".format(namespace)):
        return CstmrCdtTrfInitn.findall("{}PmtInf".format(namespace))


def get_cdttrftxinf(document, namespace):
    for pmtinf in get_pmtinf(document, namespace):
        return pmtinf.findall("{}CdtTrfTxInf".format(namespace))


def protect_PmtInf(document, group_str, _group_num, key):
    namespace = SEPA.getNamespace(document.getroot())
    protect_debitor(document, namespace, group_str, _group_num, key)
    protect_creditor(document, namespace, group_str, _group_num, key)
    protect_ultimate_debitor(document, namespace, group_str, _group_num, key)
    protect_ultimate_creditor(document, namespace, group_str, _group_num, key)
