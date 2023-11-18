# text-to-image-gen
High-performance image generation using Stable Diffusion in KerasCV

![Example Image](https://i.imgur.com/2uC8rYJ.png)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deepak7376/text-to-image-gen.git
   cd text-to-image-gen
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with the following arguments:

```bash
python src/text_to_image.py --text "photograph of an astronaut riding a horse" --batch_size 1
```

### Options

- `--text`: The text to convert to images.
- `--batch_size`: Batch size for image generation (default is 3).

## Example

```bash
python src/text_to_image.py --text "photograph of an astronaut riding a horse" --batch_size 1
```

This will generate images based on the input text and display them.
![](https://www.tensorflow.org/static/tutorials/generative/generate_images_with_stable_diffusion_files/output_-iTHsk7v3naK_1.png)

## License

This project is licensed under the [MIT License](LICENSE).
