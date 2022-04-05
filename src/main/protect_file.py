import src.file.MDTT.MDTT as mdtt
import src.file.SEPA.SEPA as sepa
import src.file.dtazv.DTAZV as dtazv
import src.file.format_check as fs
import src.file.swift_mt.swift_mt as mt


def protect_file(file_path, output_path, customer_columns_to_protect, user_columns_to_protect, account_columns_to_protect, tags_to_protect, group_str, _group_num, key):
    file_format = fs.get_file_format(file_path)
    if file_format == 'xml' or file_format == 'xsd':
        if sepa.is_sepa_format(file_path):
            sepa.protect_sepa(file_path, output_path, group_str, _group_num, key)
    elif file_format == 'txt':
        dtazv.protect_dtazv(file_path, output_path, group_str, _group_num, key)
    elif file_format == 'mt':
        mt.protect_mt_file(file_path, output_path, tags_to_protect, group_str, _group_num, key)
    elif file_format == 'csv':
        mdtt.protect_mdtt_files(file_path, output_path, customer_columns_to_protect, user_columns_to_protect, account_columns_to_protect, group_str, _group_num, key)
    else:
        print("Not supported format")
