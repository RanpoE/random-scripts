import os
import shutil

FILE_TYPES = {
    'MusicFiles': ['ogg', 'mp3', 'wav'],
    'ArchieveFiles': ['zip', '7z'],
    'ImageFiles': ['jpg', 'png', 'gif', 'jpeg', 'svg'],
    'VideoFiles': ['mov', 'mp4', '3gp', 'webm'],
    'PDFFiles': ['pdf'],
    'DataFiles': ['csv', 'json', 'md']
}

CURRENT_PATH = os.getcwd()


def checkFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


files = os.listdir(CURRENT_PATH)
for file in files:
    extension = os.path.splitext(file)[1][1:]
    src = os.path.join(CURRENT_PATH, file)
    for key, val in FILE_TYPES.items():
        if extension in val:
            dst = checkFolder(os.path.join(CURRENT_PATH, key))
            shutil.move(src, dst)
