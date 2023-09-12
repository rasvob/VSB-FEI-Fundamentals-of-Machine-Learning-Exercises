import os
import shutil
import sys
from dotenv import load_dotenv

def copy_files_with_prefix(prefix, src_dir, dst_dir):
    """
    Copy files from src_dir to dst_dir if they start with prefix
    """
    for file in os.listdir(src_dir):
        if file.startswith(prefix):
            shutil.copy(os.path.join(src_dir, file), dst_dir)

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Load environment variables
    src_dir = os.getenv("INPUT_PATH")
    dst_dir = os.getenv("OUTPUT_PATH")
    prefix = os.getenv("PREFIX")

    # Copy files
    copy_files_with_prefix(prefix, src_dir, dst_dir)







