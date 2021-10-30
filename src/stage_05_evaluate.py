from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import load_full_model, get_unique_path_to_save_model
from src.utils.callbacks import get_callbacks
from src.utils.data_management import train_valid_generator
import argparse
import os
import shutil

import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
# create_directory([log_dir])
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir, "running_logs.log"), level=logging.INFO, format=logging_str, filemode="a")

def evaluate(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    
    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>>>>>>>>> stage 05 evaluate >>>>>>>>>>>>>>>")
        evaluate(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("<<<<< stage 05 complete! model evaluation complete <<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
