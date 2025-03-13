"""
This a program to list out directories 
as well as view the contents of a file
after the full path to the directory or
file is input by the user.
"""

import os

def main():
    path = input("Please enter the path to the file or directory you would like to view: ")
    if os.path.isdir(path):
        view_directory(path)
    elif os.path.isfile(path):
        view_file(path)
    else:
        print("Invalid path or file doesn't exist.")
        input("Press Enter to Quit!")

def view_directory(path):
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "':")
    for name in dir_list:
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):  # If it's a directory, recurse
            print(f"Directory: {name}")
            view_directory(full_path)  # Recursive call
        else:  # If it's a file, display the file
            print(f"File: {name}")
            view_file(full_path)  # Call to display the file

def view_file(path):
    print(f"\nContents of file: {path}")
    with open(path, 'r') as f:  # Correctly open the file in read mode
        print(f.read())  # Display file content

if __name__ == "__main__":
    main()

