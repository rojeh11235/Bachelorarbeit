import configparser

from src.main.protect_file import protect_file

config = configparser.ConfigParser()
config.read("C:\\NAK\\BachelorArbeit\\Filesprotecter\\config\\ConfigFile.cfg")


def main():
    file_path = config.get('Section1', 'file_path')
    with open(file_path) as f:
        file_path = f.readlines()[0]
    protect_file(file_path)


if __name__ == "__main__":
    main()
