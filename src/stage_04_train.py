from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import load_full_model
from src.utils.callbacks import get_callbacks
import argparse
import os
import shutil

import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
# create_directory([log_dir])
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir, "running_logs.log"), level=logging.INFO, format=logging_str, filemode="a")

def train_model(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]

    train_model_dir_path = os.path.join(artifacts_dir, artifacts["TRAINED_MODEL_DIR"])
    
    create_directory([train_model_dir_path])

    untrained_full_model_path = os.path.join(artifacts_dir, artifacts["BASE_MODEL_DIR"], artifacts["UPDATED_BASE_MODEL_NAME"])

    model = load_full_model(untrained_full_model_path)

    callback_dir_path = os.path.join(artifacts_dir, artifacts["CALLBACKS_DIR"])
    callbacks = get_callbacks(callback_dir_path)

    # train_generator





if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    
    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>>>>>>>>> stage 04 started >>>>>>>>>>>>>>>")
        train_model(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("<<<<< stage 04 complete! model training is complete and model is saved <<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e