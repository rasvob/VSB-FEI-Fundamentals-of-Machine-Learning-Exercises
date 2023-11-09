import os
import shutil
import sys
from dotenv import load_dotenv, dotenv_values

def copy_files_with_prefix(prefix, src_dir, dst_dir):
    """
    Copy files from src_dir to dst_dir if they start with prefix
    """
    for file in os.listdir(src_dir):
        if file.startswith(prefix):
            shutil.copy(os.path.join(src_dir, file), dst_dir)
            print(f"Copying {file} to {dst_dir}")

def copy_using_env(env_path='.env'):
    config = dotenv_values(env_path)

    # Load environment variables
    src_dir = config["INPUT_PATH"]
    dst_dir = config["OUTPUT_PATH"]
    prefix = config["PREFIX"]

    # Copy files
    copy_files_with_prefix(prefix, src_dir, dst_dir)


if __name__ == "__main__":
    # Load environment variables from .env file

    tasks = ['.env', '.env.eng']
    for task in tasks:
        print(f"Copying {task}")
        copy_using_env(task)