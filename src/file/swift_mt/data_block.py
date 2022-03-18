import re
from src.file.swift_mt import pattern


def get_data_block(message):
    return re.search(pattern.data_block_pat, message).group(0)



