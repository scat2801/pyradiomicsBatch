import tkinter as tk
from tkinter import filedialog

import os, sys, glob, csv

def locateFolder():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    return folder_path

def folderNav(folder_path):
    csv_path = folder_path + os.sep + 'database.csv'
    f = open (csv_path, 'w')
    writer = csv.writer(f)
    row = ['ID', 'Image', 'Mask']
    writer.writerow(row)

    subfolders = [ f.path for f in os.scandir(folder_path) if f.is_dir() ]
    sf_cleaned = list(subfolders)
    for i in range(len(subfolders)):
        sf_cleaned[i]   = subfolders[i].split(os.sep)[-1]
        file_list = os.listdir(subfolders[i])
        maxMaskFileSize = 0

        file_name = list(file_list)
        for j in range(len(file_list)):
            file_name [j] = file_list[j].split('.nii')[0]

        for j in range(len(file_list)):
            if 'nii' in file_list[j]:
                if file_name[j] == min(file_name, key=len):
                    if maxMaskFileSize >  os.path.getsize(subfolders[i] + os.sep + file_list[j]):
                        sys.exit('Inconsistent file size/name, check:' + sf_cleaned[i])
                    else:
                        col_two = './' + sf_cleaned[i] + os.sep + file_list[j]
                else:
                    maxMaskFileSize = os.path.getsize(subfolders[i] + os.sep + file_list[j])
                    col_three = './' + sf_cleaned[i] + os.sep + file_list[j]
            if j >= 1:
                row = [sf_cleaned[i], col_two, col_three]
                writer.writerow(row)
    f.close()

if __name__ == "__main__":
    folder_path = locateFolder()
    folderNav(folder_path)

