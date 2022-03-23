# GroupHeader
debitor_name_xpath = "Document\CstmrCdtTrfInitn\InitgPty\Nm"
debitor_adresse_xpath = "Document\CstmrCdtTrfInitn\InitgPty\PstlAdr\Adrline"  # Adress Line kann mehrmal vorkommen
# PaymentInformation
debitor_name_xpath = "Document\CstmrCdtTrfInitn\PmtInf\Dbtr\Nm"
debitor_adresse_xpath = "Document\CstmrCdtTrfInitn\PmtInf\Dbtr\PstAdr\Adrline"  # Adress Line kann mehrmal vorkommen
debitor_account = "Document\CstmrCdtTrfInitn\PmtInf\DbtrAcct\Id\IBAN"
ultimate_debitor_name = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\UltmtDbtr\Nm"
ultimate_debitor_Adresse = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\UltmtDbtr\PstAdr\Adrline"  # Adress Line kann mehrmal vorkommen
creditor_name_xpath = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\Cdtr\Nm"
creditor_adresse_xpath = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\Cdtr\PstAdr\Adrline"  # Adress Line kann mehrmal vorkommen
creditor_account_xpath = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\CdtrAcct\Id\IBAN"
ultimate_creditor_name_xpath = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\UltmtCdtr\Nm"
ultimate_creditor_Adresse_xpath = "Document\CstmrCdtTrfInitn\PmtInf\CdtTrfTxInf\UltmtCDTR\PstAdr\Adrline"  # Adress Line kann mehrmal vorkommen"
