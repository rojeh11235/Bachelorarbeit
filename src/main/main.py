import configparser

from src.encryption import rot_random
from src.main.protect_file import protect_file

config = configparser.ConfigParser()
config.read("../../config/config.ini")


def main():
    output_path = config.get('PATH', 'output_path')
    group_str_path = config.get('ENCRYPTION', 'group_str_path')
    group_num_path = config.get('ENCRYPTION', 'group_num_path')
    key = config.get('ENCRYPTION', 'key')
    file_paths = config.get('PATH', 'file_path').split(',')
    customer_columns_to_protect = config.get('MDTT', 'customer_columns_to_protect').split(',')
    user_columns_to_protect = config.get('MDTT', 'user_columns_to_protect').split(',')
    account_columns_to_protect = config.get('MDTT', 'account_columns_to_protect').split(',')
    tags_to_protect = config.get('MT', 'tags_to_protect').split(',')
    group_str = rot_random.random_str_group(group_str_path)
    group_num = rot_random.random_numeric_group(group_num_path)
    for file_path in file_paths:
        protect_file(file_path, output_path, customer_columns_to_protect,user_columns_to_protect,account_columns_to_protect, tags_to_protect, group_str, group_num, key)


if __name__ == "__main__":
    main()
