import os
import shutil
import sys
import zipfile

EXTRACT_PATH = './minecraft'

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Usage: python xxx.py [targetZip] [commitMsgFile]')
        sys.exit(0)
    zip_path = sys.argv[1]
    commit_msg = sys.argv[2]

    del_list = os.listdir(EXTRACT_PATH)
    for pth in del_list:
        file_path = os.path.join(EXTRACT_PATH, pth)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall("./minecraft")

    # os.system('git add --renormalize .')
    os.system('git add -A')
    os.system('git commit -m {} -q'.format(commit_msg))
