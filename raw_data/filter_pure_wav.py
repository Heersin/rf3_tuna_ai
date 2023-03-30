import argparse
import os
from tinytag import TinyTag


def main():
    parser = argparse.ArgumentParser(description='Traverse a folder and filter out WAV files whose titles do not contain "myce".')
    parser.add_argument('folder', help='the folder to traverse')
    
    args = parser.parse_args()

    folder_path = args.folder
    cnt = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            fpath = os.path.join(folder_path, filename)
            audio = TinyTag.get(fpath)
            title = audio.title
            if title is None or 'myce' in title:
                to_be_deleted = fpath
                print("[deleting]: {}".format(to_be_deleted))
                print("\ttitle : {}".format(title))
                os.remove(to_be_deleted)
            else:
                new_path = "{}.wav".format(cnt)
                cnt += 1
                new_path = os.path.join(folder_path, new_path)
                print("{} -> {}".format(fpath, new_path))
                os.rename(fpath, new_path)

if __name__ == '__main__':
    main()
