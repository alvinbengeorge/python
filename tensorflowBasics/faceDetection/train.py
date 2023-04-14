import tensorflow as tf
import numpy as np
import cv2


data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1. / 255,
    validation_split=0.2
)
