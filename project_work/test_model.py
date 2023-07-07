from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


def model_evaluate(image):

    BASE_PATH = r"E:\Code\SSAIthread_2023\models\garbage-model"

    MODEL_PATH = BASE_PATH + r"\keras_model.h5"
    LABELS_PATH = BASE_PATH + r"\labels.txt"

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(MODEL_PATH, compile=False)

    # Load the labels
    class_names = open(LABELS_PATH, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score



"""
BASE_PATH = r"E:\Code\SS_AI_2023\models\garbage-model"

MODEL_PATH = BASE_PATH + r"\keras_model.h5"
LABELS_PATH = BASE_PATH + r"\labels.txt"

TEST_IMAGE_PATH = r"E:\Code\SS_AI_2023\datasets\garbage-imgs\test\test_plastic_1.jpg"

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(MODEL_PATH, compile=False)

# Load the labels
class_names = open(LABELS_PATH, "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(TEST_IMAGE_PATH).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]
"""

TEST_IMAGE_PATH = r"E:\Code\SSAIthread_2023\datasets\garbage-imgs\test\test_plastic_1.jpg"
image = Image.open(TEST_IMAGE_PATH).convert("RGB")

class_name, confidence_score = model_evaluate(image)

# Print prediction and confidence score
print("Class:", class_name, end="")
print("Confidence Score:", confidence_score)
