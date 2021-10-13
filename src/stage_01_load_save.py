from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd 
import os
import shutil
from tqdm import tqdm


def copy_file(source_download_dir, local_path_dir):
    list_of_files = os.listdir(source_download_dir)
    N = len(list_of_files)
    for file in tqdm(list_of_files, total=N, desc=f'copying file from {source_download_dir} to {local_path_dir}', colour="green"):
        src =  os.path.join(source_download_dir, file)
        dest = os.path.join(local_path_dir, file)
        shutil.copy(src, dest)


def get_data(config_path):
    configcopy_file(source_download_dir, local_path_dir) = read_yaml(config_path)
    
    source_download_dirs = config["source_download_dirs"]
    local_path_dirs = config["local_path_dirs"]


    for source_download_dir, local_path_dir in tqdm(zip(source_download_dirs, local_path_dirs), total=2, desc="list of folders"):
        create_directory([local_path_dir])
        


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    
    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
