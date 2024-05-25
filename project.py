from argparse import FileType
import os
from pathlib import Path

SUCCESS = 0
NOT_FOUND = 1

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return SUCCESS, category
    return NOT_FOUND, 'SCRIPT'

def organizeDirectory():
    for items in os.scandir():
        if items.is_dir():
            continue

        filePath = Path(items)
        fileType = filePath.suffix.lower()
        status_code, category = pickDirectory(fileType)

        if status_code == SUCCESS:
            directoryPath = Path(category)
            if directoryPath.is_dir() != True:
                directoryPath.mkdir()
            filePath.rename(directoryPath.joinpath(filePath))
            print(f"Successfully categorized as {category}")
        #else:
           # print(f"Couldn't categorize {filePath.name}")

organizeDirectory()
