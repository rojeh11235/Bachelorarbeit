from src.file.SEPA import SEPA


def protect_debitor(document, namespace):
    for pmttpinf in get_pmtinf(document, namespace):
        for dbtr in pmttpinf.findall("{}Dbtr".format(namespace)):
            protect_postal_adresse(dbtr, namespace)
            for name in dbtr.findall("{}Nm".format(namespace)):
                name.text = 'protected_name'
        protect_account(pmttpinf, "DbtrAcct", namespace)


def protect_creditor(document, namespace):
    for pmttpinf in get_pmtinf(document, namespace):
        for cdttrftxinf in pmttpinf.findall("{}CdtTrfTxInf".format(namespace)):
            for Cdtr in cdttrftxinf.findall("{}Cdtr".format(namespace)):
                protect_postal_adresse(Cdtr, namespace)
                for name in Cdtr.findall("{}Nm".format(namespace)):
                    name.text = 'protected_name'
            protect_account(cdttrftxinf, "CdtrAcct", namespace)


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


def protect_ultimate_debitor(document, namespace):
    for CdtTrfTxInf in get_cdttrftxinf(document, namespace):
        for UltmtDbtr in CdtTrfTxInf.findall("{}UltmtDbtr".format(namespace)):
            protect_postal_adresse(UltmtDbtr, namespace)
            for name in UltmtDbtr.findall("{}Nm".format(namespace)):
                name.text = 'protected_name'
        protect_account(CdtTrfTxInf, "UltmtDbtrAcc", namespace)


def protect_ultimate_creditor(document, namespace):
    for CdtTrfTxInf in get_cdttrftxinf(document, namespace):
        for UltmtCdtr in CdtTrfTxInf.findall("{}UltmtCdtr".format(namespace)):
            protect_postal_adresse(UltmtCdtr, namespace)
            for name in UltmtCdtr.findall("{}Nm".format(namespace)):
                name.text = 'protected_name'
        protect_account(CdtTrfTxInf, "UltmtDbtrAcc", namespace)


def get_pmtinf(document, namespace):
    for CstmrCdtTrfInitn in document.findall("{}CstmrCdtTrfInitn".format(namespace)):
        return CstmrCdtTrfInitn.findall("{}PmtInf".format(namespace))


def get_cdttrftxinf(document, namespace):
    for pmtinf in get_pmtinf(document, namespace):
        return pmtinf.findall("{}CdtTrfTxInf".format(namespace))


def protect_PmtInf(document):
    namespace = SEPA.getNamespace(document.getroot())
    protect_debitor(document, namespace)
    protect_creditor(document, namespace)
    protect_ultimate_debitor(document, namespace)
    protect_ultimate_creditor(document, namespace)
