import os
import csv
from datetime import datetime

def createCsvFile(path, name):
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        field = ['file_path', 'file_size', 'creation_date', 'file_type']
        listOfDir = filesMetadata(path)
        
        writer.writerow(field)
        
        for listName, item in listOfDir.items():
            writer.writerow(item)       
        

def filesMetadata(path):
    dirsDic = {}
    
    for name in os.listdir(dirInput):
        filePath = os.path.join(dirInput, name)
        stats = os.stat(filePath)
        fileName, fileExt = os.path.splitext(name)
        
        attr = [
            path + name,
            stats.st_size,
            timeConvert(stats.st_birthtime),
            fileExt,
        ]
    
        dirsDic[name] = attr
        
    return dirsDic

def timeConvert(time):
    newTime = datetime.fromtimestamp(time)
    return newTime.date()

if __name__ == "__main__":
    dirInput = input("Enter the directory path to scan: ")
    isSaveFile = input("Want save? y/n: ")
    
    createCsvFile(dirInput, 'test.csv')
    
    if (isSaveFile == 'y'):
        nameFile = input("Enter file name: ")
        createCsvFile(dirInput, nameFile)
    elif (isSaveFile == 'n'):
        print("Bye!")
    else:
        print("Bye!")
