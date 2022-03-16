from src.main.protect_file import protect_file


def main():
    print("Enter filepath")
    with open('C:\\NAK\\BachelorArbeit\\Filesprotecter\\config\\filepath.txt') as f:
        file_path = f.readlines()[0]
    protect_file(file_path )


if __name__ == "__main__":
    main()
