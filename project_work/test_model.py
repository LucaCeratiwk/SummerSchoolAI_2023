from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# change this based on your local repo path
import sys
sys.path.append('./local/')
from config import REPO_ABSOLUTE_PATH

# modify to select a new model
model_foldername = r'\models\garbage-model'

MODEL_PATH = REPO_ABSOLUTE_PATH + model_foldername + r"\keras_model.h5"
LABELS_PATH = REPO_ABSOLUTE_PATH + model_foldername + r"\labels.txt"

def model_evaluate(image_path):

    # open image
    image = Image.open(image_path).convert("RGB")

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


TEST_IMAGE_PATH = REPO_ABSOLUTE_PATH + r"\datasets\garbage-imgs\test\test_plastic_1.jpg"
class_name, confidence_score = model_evaluate(TEST_IMAGE_PATH)

# Print prediction and confidence score
print("Class:", class_name, end="")
print("Confidence Score:", confidence_score)
