import tensorflow as tf
import numpy as np, matplotlib.pyplot as plt

fashionDataset = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashionDataset.load_data()

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]


def showTrainImage(index: int):
    plt.figure()
    plt.imshow(x_train[index])
    plt.show()
    return x_train[index]


x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10),

    ]
)
lossFunction = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer="adam", loss=lossFunction, metrics=["accuracy"])

model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test, y_test, verbose=2)


def makePrediction(model: tf.keras.Sequential, index: int):
    probabilityModel = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probabilityModel.predict(x_test)
    return np.argmax(predictions[index]) == y_test[index]


print("Index 1 image prediction is ", makePrediction(model, 1))