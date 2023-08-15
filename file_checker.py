import os
import shutil

FILE_TYPES = {
    'text': ['txt', 'me'],
    'image': ['jpg', 'png', 'gif'],
    'script': ['py', 'js']
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
            shutil.copy(src, dst)
