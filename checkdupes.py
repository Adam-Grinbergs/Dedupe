"""Given a starting folder, recurse and check every file and create a list
of files and their hash values. Identify duplicates using md5 checksum"""

import os
import hashlib
from collections import defaultdict
from tqdm import tqdm
import csv

src_folder = r'F:'

def generate_md5(fname, chunk_size=1024):
    """
    Function which takes a file name and returns md5 checksum of the file
    """
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        chunk = f.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)
    #Return the hex checksum
    return hash.hexdigest()

if __name__ == "__main__":
    file_types_inscope = ["ppt", "pptx", "pdf", "txt", "html","mp4", "jpg", 
                          "png", "xls", "xlsx", "xml","vsd", "py", "json"]
    md5_dict = defaultdict(list)

    for path, dirs, files in tqdm(os.walk(src_folder)):
        for file in files:
            if file.endswith(tuple(file_types_inscope)):
                file_path = os.path.join(os.path.abspath(path), file)
                try:
                    md5_dict[generate_md5(file_path)].append(file_path)
                except:
                    pass

    duplicate_files = (
        val for key, val in md5_dict.items() if len(val) > 1)
    
    with open("duplicates.csv", "w") as log:
        csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL, delimiter=",",
        lineterminator="\n")
        header = ["File Names"]
        csv_writer.writerow(header)

        for file_name in duplicate_files:
            csv_writer.writerow(file_name)
