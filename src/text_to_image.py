import argparse
import matplotlib.pyplot as plt
import keras_cv
from tensorflow import keras

def text_to_image_cli(text, batch_size):
    # Implement your text_to_image function here or call it from the module
    model = keras_cv.models.StableDiffusion(img_width=224, img_height=224)
    images = model.text_to_image(text, batch_size)
    plot_images(images)
    plt.show()

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to image and plot it.")
    parser.add_argument("--text", type=str, help="Text to convert to image")
    parser.add_argument("--batch_size", type=int, default=3, help="Batch size for image generation")

    args = parser.parse_args()

    text_to_image_cli(args.text, args.batch_size)
