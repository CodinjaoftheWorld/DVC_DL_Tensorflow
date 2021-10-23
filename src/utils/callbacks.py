import time
import os
import tensorflow as tf
import joblib
import logging
from src.utils.all_utils import get_timestamp



def create_and__save_tensorboard_callback(callbacks_dir, tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callbacks = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    tb_callback_filepath = os.path.join(callbacks_dir, "tensorboard_cb.cb")
    joblib.dump(tensorboard_callbacks, tb_callback_filepath)
    loggign.info(f"tensorboard callback is being saved at {tb_callback_filepath}")



def create_and__save_checkpoint_callback(callbacks_dir, checkpoint_dir):
    pass
