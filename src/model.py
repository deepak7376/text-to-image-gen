import keras_cv
from tensorflow import keras

def load_model():
    model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
    return model