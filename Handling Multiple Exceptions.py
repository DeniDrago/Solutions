def handling_multiple_exception():
    try:
        filename = input("Enter a file name: ")
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    print(num * 2)
                except ValueError:
                    print("The file contains non-numeric values!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("The program does not have permission to access the file!")
    finally:
        print("The program has successfully completed its work.")


handling_multiple_exception()
