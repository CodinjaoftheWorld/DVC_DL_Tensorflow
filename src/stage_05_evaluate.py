from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import load_trained_model, true_classes, class_labels, report
from src.utils.callbacks import get_callbacks
from src.utils.data_management import test_gen
from sklearn.metrics import classification_report, confusion_matrix
import argparse
import os
import shutil
import tensorflow as tf
import logging
import numpy as np
import matplotlib.pyplot as plt


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

    trained_model_path = os.path.join(artifacts_dir, artifacts["TRAINED_MODEL_DIR"])
    
    full_trianed_model_path = "".join([os.path.join(trained_model_path, h5_file) for h5_file in os.listdir(trained_model_path) if h5_file.endswith(".h5")])

    model = load_trained_model(full_trianed_model_path)

    callback_dir_path = os.path.join(artifacts_dir, artifacts["CALLBACKS_DIR"])
    callbacks = get_callbacks(callback_dir_path)   

    testing_generator = test_gen(
        test_dir = artifacts["TEST_DIR"], 
        IMAGE_SIZE = tuple(params["IMAGE_SIZE"][:-1]), 
        TEST_BATCH_SIZE = params["TEST_BATCH_SIZE"]
        )
    testing_generator.reset()

    labels = ["cat", "dog"]
    predictions = model.predict(testing_generator)
    predictions = np.argmax(predictions, axis=1)

    trueClasses = true_classes(testing_generator)
    classLabels = class_labels(testing_generator)   
    
    # classification report
    cls_report = report(trueClasses, classLabels, predictions)
    logging.info(f"Classification Report: \n{cls_report}")

    # confusion matrix
    cm = confusion_matrix(trueClasses, predictions)
    logging.info(f"Confusion Matrix: \n{cm}")


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
