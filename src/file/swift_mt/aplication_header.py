import re
from src.file.swift_mt import pattern


def get_application_header(message):
    return re.search(pattern.application_header_pat, message).group(0)
