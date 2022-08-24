import shutil
from glob import glob
import os

extension = '.dat'
pattern1 = 'E1-2F-S10-NXT'
pattern2 = 'E1-2F-S05-NXT'
separator = '/'


def get_files(my_path):
    return (
        y.replace('\\', separator)
        for x in os.walk(my_path)
        for y in glob(os.path.join(x[0], '*{}'.format(extension)))
    )


def copy_files(dst1, dst2, data_folder):
    result = get_files(data_folder)
    if not os.path.exists(dst1):
        os.makedirs(dst1)

    if not os.path.exists(dst2):
        os.makedirs(dst2)

    for file_name in result:
        fname = file_name.split(separator)[-1]

        if pattern1 in file_name:
            shutil.copy(file_name, os.path.join(dst1, fname))
        elif pattern2 in file_name:
            shutil.copy(file_name, os.path.join(dst2, fname))
