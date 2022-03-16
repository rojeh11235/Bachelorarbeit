from src.file.SEPA import SEPA


def protect_basic_account(document, namespace):
    for stmt in document.iter("{}Stmt".format(namespace)):
        protect_account(stmt, 'Acct', namespace)


def protect_related_account(document, namespace):
    for stmt in document.iter("{}Stmt".format(namespace)):
        protect_account(stmt, 'RltdAcc', namespace)


def protect_debitor(document, namespace):
    for Ntry in get_ntry(document, namespace):
        for related_parties in get_related_parties(Ntry, namespace):
            for Dbtr in related_parties.findall("{}Dbtr".format(namespace)):
                protect_postal_adresse(Dbtr, namespace)
                for name in Dbtr.findall("{}Nm".format(namespace)):
                    name.text = 'protected_name'
            protect_account(related_parties, "DbtrAcct", namespace)


def protect_creditor(document, namespace):
    for Ntry in get_ntry(document, namespace):
        for related_parties in get_related_parties(Ntry, namespace):
            for Cdtr in related_parties.findall("{}Cdtr".format(namespace)):
                protect_postal_adresse(Cdtr, namespace)
                for name in Cdtr.findall("{}Nm".format(namespace)):
                    name.text = 'protected_name'
            protect_account(related_parties, "CdtrAcct", namespace)


def get_related_parties(Ntry, namespace):
    for NtryDtls in Ntry.findall("{}NtryDtls".format(namespace)):
        for TxDtls in NtryDtls.findall("{}TxDtls".format(namespace)):
            return TxDtls.findall("{}RltdPties".format(namespace))


def get_ntry(document, namespace):
    for stmt in document.iter("{}Stmt".format(namespace)):
        return stmt.findall("{}Ntry".format(namespace))


def protect_postal_adresse(adresse_owner, namespace):
    for pstladr in adresse_owner.findall("{}PstlAdr".format(namespace, )):
        for adrline in pstladr.findall("{}AdrLine".format(namespace)):
            adrline.text = adrline.text + 'AdrLine_protected'


def protect_account(_stmt, _account, namespace):
    for acc in _stmt.iter("{}{}".format(namespace, _account)):
        for account_name in acc.findall("{}Nm".format(namespace)):
            account_name.text = 'konto_name_protected'
        for account_owner in acc.findall("{}Ownr".format(namespace)):
            for owner_name in account_owner.findall("{}Nm".format(namespace)):
                owner_name.text = 'account_owner_name'
            protect_postal_adresse(account_owner, namespace)
        for id in acc.findall("{}Id".format(namespace)):
            for iban in id.findall("{}IBAN".format(namespace)):
                iban.text = 'IBAN_Protected'


def protect_stmt(document):
    document.getroot()
    namespace = SEPA.getNamespace(document.getroot())
    protect_basic_account(document, namespace)
    protect_related_account(document, namespace)
    protect_debitor(document, namespace)
    protect_creditor(document, namespace)
