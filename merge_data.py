import os
import shutil

PATH = 'SPECIFY_YOUR_DATA_PATH'
TARGET = 'SPECIFY_YOUR_TARGET_PATH'

def move_file(src, target):
    print(f'move: {src} -> {target}')
    shutil.move(src, target)

def merge_files(src, target):
    src_list = os.listdir(src)
    trg_list = os.listdir(target)
    
    duplicate_files = []
    for f in sorted(src_list):
        if f not in trg_list:
            move_file(os.path.join(src, f), target)
        else:
            duplicate_files.append(os.path.join(f))
    if not duplicate_files:
        shutil.rmtree(src)
    return src, duplicate_files

if __name__ == "__main__":

    for p in [p for p in os.listdir(PATH) if p.startswith('Clinical DBS')]:
        path_ = os.path.join(PATH, p)
        clean_list = sorted(
            [x for x in os.listdir(path_)
                if not x.startswith('.') and not x.endswith('.xlsx')],
            key=lambda x: int(x))
        for p_ in clean_list:
            src_path = os.path.join(path_, p_)
            trg_list = os.listdir(TARGET)
            if p_ in trg_list:
                merge_files(src_path, os.path.join(TARGET, p_))
            else:
                move_file(src_path, TARGET)

        src_list = [f for f in os.listdir(path_) if not f.startswith('.')]
        if not src_list:
            shutil.rmtree(path_)
