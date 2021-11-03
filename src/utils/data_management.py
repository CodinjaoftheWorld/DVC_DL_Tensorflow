import tensorflow as tf
import logging

def train_valid_generator(data_dir, IMAGE_SIZE, BATCH_SIZE, do_data_augmentation):
    
    datagenerator_kwargs = dict(
        rescale=1./255,
        validation_split=0.20
    )

    dataflow_kwargs = dict(
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        interpolation="bilinear"
    )

    valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

    valid_generator = valid_datagenerator.flow_from_directory(
        directory=data_dir,
        subset="validation",
        shuffle=False,
        **dataflow_kwargs
    )

    if do_data_augmentation:
        train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range=40,
            horizontal_flip=True,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            **datagenerator_kwargs
        )
        logging.info(f"data autmentation is used for trainig")
    else:
        train_datagenerator = valid_datagenerator
        logging.info(f"data autmentation is NOT used for trainig")

    train_generator = train_datagenerator.flow_from_directory(
        directory=data_dir,
        subset="training",
        shuffle=True,
        **dataflow_kwargs   
    )

    logging.info(f"train and valid generator are created")
    return train_generator, valid_generator



def test_gen(test_dir, IMAGE_SIZE, TEST_BATCH_SIZE):

    test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

    test_generator = test_datagenerator.flow_from_directory(
        directory=test_dir,
        target_size=IMAGE_SIZE,
        shuffle=False,
        batch_size=TEST_BATCH_SIZE
        )

    # test_dataset = tf.keras.utils.image_dataset_from_directory(test_dir,
    #                                                         shuffle=False,
    #                                                         batch_size=TEST_BATCH_SIZE,
    #                                                         image_size=IMAGE_SIZE)

    logging.info(f"$$$$$$$$$  testing generator is created  $$$$$$$$$$")
    return test_generator

