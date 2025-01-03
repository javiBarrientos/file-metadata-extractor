"""Module providing a function os."""

import os
import csv
from datetime import datetime

def create_csv_file(path, name) -> None:
    """Function create csv file."""

    with open(name, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, dialect='excel')
        field = ['file_path', 'file_size', 'creation_date', 'file_type']
        list_of_dir = files_metadata(path)
        writer.writerow(field)

        for _, item in list_of_dir.items():
            writer.writerow(item)

def files_metadata(path) -> dict:
    """Function returning date time formated."""

    dirs_dic = {}
    for name in os.listdir(path):
        file_path = os.path.join(path, name)
        stats = os.stat(file_path)
        _, file_ext = os.path.splitext(name)

        attr = [
            path + name,
            stats.st_size,
            time_convert(stats.st_birthtime),
            file_ext,
        ]

        dirs_dic[name] = attr

    return dirs_dic

def time_convert(time) -> datetime:
    """Function returning date time formated."""

    new_time = datetime.fromtimestamp(time)
    return new_time.date()

if __name__ == "__main__":
    dir_input = input("Enter the directory path to scan: ")
    is_save_file = input("Want save? y/n: ")

    if is_save_file == 'y':
        name_file = input("Enter file name: ")
        create_csv_file(dir_input, name_file)

    elif is_save_file == 'n':
        print("Bye!")

    else:
        print("Bye!")
