import os
import pathlib

def get_file_format(file_path):
    split_file =os.path.splitext(file_path)
    return split_file[1][1:]
