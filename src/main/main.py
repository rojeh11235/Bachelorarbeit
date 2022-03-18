import configparser

from src.main.protect_file import protect_file

config = configparser.ConfigParser()
config.read("C:\\NAK\\BachelorArbeit\\Filesprotecter\\config\\ConfigFile.cfg")


def main():
    file_paths = config.get('Section1', 'file_path').split(',')
    columns_to_protect = config.get('Section1', 'columns_to_protect').split(',')
    tags_to_protect = config.get('Section1', 'tags_to_protect').split(',')
    for file_path in file_paths:
        protect_file(file_path,columns_to_protect, tags_to_protect)


if __name__ == "__main__":
    main()

