import re
import pattern


def get_user_header(message):
    return re.search(pattern.user_header_pat, message).group(0)