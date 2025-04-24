import os
import shutil

source = "subdir1/example.txt"
destination_dir = "subdir2"

os.makedirs(destination_dir, exist_ok=True)
shutil.copy(source, os.path.join(destination_dir, "example.txt"))
