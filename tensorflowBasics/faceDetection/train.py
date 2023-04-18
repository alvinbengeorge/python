import tensorflow as tf
import numpy as np
import cv2


data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1. / 255,
    validation_split=0.2
)

train_generator = data_generator.flow_from_directory(
    'images',
    target_size=(200, 200),
    batch_size=32,
)

validation_generator = data_generator.flow_from_directory(
    'images',
    target_size=(200, 200),
    batch_size=32,
)