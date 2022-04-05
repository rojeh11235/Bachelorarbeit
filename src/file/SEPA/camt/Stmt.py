from src.encryption import rot_random
from src.file.SEPA import SEPA


def protect_basic_account(document, namespace, group_str, _group_num, key):
    for stmt in document.iter("{}Stmt".format(namespace)):
        protect_account(stmt, 'Acct', namespace, group_str, _group_num, key)


def protect_related_account(document, namespace, group_str, _group_num, key):
    for stmt in document.iter("{}Stmt".format(namespace)):
        protect_account(stmt, 'RltdAcc', namespace, group_str, _group_num, key)


def protect_debitor(document, namespace, group_str, _group_num, key):
    for Ntry in get_ntry(document, namespace):
        for related_parties in get_related_parties(Ntry, namespace):
            for Dbtr in related_parties.findall("{}Dbtr".format(namespace)):
                protect_postal_adresse(Dbtr, namespace, group_str, _group_num, key)
                for name in Dbtr.findall("{}Nm".format(namespace)):
                    name.text = rot_random.de_rot_random(name.text, group_str, _group_num, key)
            protect_account(related_parties, "DbtrAcct", namespace, group_str, _group_num, key)


def protect_creditor(document, namespace, group_str, _group_num, key):
    for Ntry in get_ntry(document, namespace):
        for related_parties in get_related_parties(Ntry, namespace):
            for Cdtr in related_parties.findall("{}Cdtr".format(namespace)):
                protect_postal_adresse(Cdtr, namespace, group_str, _group_num, key)
                for name in Cdtr.findall("{}Nm".format(namespace)):
                    name.text = rot_random.de_rot_random(name.text, group_str, _group_num, key)
            protect_account(related_parties, "CdtrAcct", namespace, group_str, _group_num, key)


def get_related_parties(Ntry, namespace):
    for NtryDtls in Ntry.findall("{}NtryDtls".format(namespace)):
        for TxDtls in NtryDtls.findall("{}TxDtls".format(namespace)):
            return TxDtls.findall("{}RltdPties".format(namespace))


def get_ntry(document, namespace):
    for stmt in document.iter("{}Stmt".format(namespace)):
        return stmt.findall("{}Ntry".format(namespace))


def protect_postal_adresse(adresse_owner, namespace, group_str, _group_num, key):
    for pstladr in adresse_owner.findall("{}PstlAdr".format(namespace, )):
        for adrline in pstladr.findall("{}AdrLine".format(namespace)):
            adrline.text = rot_random.de_rot_random(adrline.text, group_str, _group_num, key)


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
                iban.text = rot_random.de_rot_random(iban.text, group_str, _group_num, key)


def protect_stmt(document, group_str, _group_num, key):
    document.getroot()
    namespace = SEPA.getNamespace(document.getroot())
    protect_basic_account(document, namespace, group_str, _group_num, key)
    protect_related_account(document, namespace, group_str, _group_num, key)
    protect_debitor(document, namespace, group_str, _group_num, key)
    protect_creditor(document, namespace, group_str, _group_num, key)
