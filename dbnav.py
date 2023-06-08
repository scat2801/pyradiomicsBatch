import tkinter as tk
from tkinter import filedialog
import os, csv

def locateFolder():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    return folder_path

def folderNav(folder_path):
    csv_path = os.getcwd() + os.sep + 'database.csv'
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
        fileSizeIter = 0

        file_name = list(file_list)
        col_two = ''
        col_three = ''
        max_file_id = 0;

        print(file_list)

        for j in range(len(file_list)):
            file_name[j] = file_list[j].split('.nii')[0]
            fileSizeIter = os.path.getsize(subfolders[i] + os.sep + file_list[j])
            if (fileSizeIter > maxMaskFileSize):
                maxMaskFileSize = fileSizeIter
                max_file_id = j
            if 'nii' in file_list[j]:
                if 'nii.gz' not in file_list[j]:
                    print ("All files need to be in .nii.gz format, please check case", file_list[j])

        for j in range(len(file_list)):
            if 'nii' in file_list[j]:
                if (j == max_file_id):
                    col_two = folder_path + os.sep + sf_cleaned[i] + os.sep + file_list[j]
                    break

        for j in range(len(file_list)):
            if 'nii' in file_list[j]:
                if (j != max_file_id):
                    col_three = folder_path + os.sep + sf_cleaned[i] + os.sep + file_list[j]
                    row = [sf_cleaned[i], col_two, col_three]
                    writer.writerow(row)
    f.close()

if __name__ == "__main__":
    folder_path = locateFolder()
    folderNav(folder_path)

