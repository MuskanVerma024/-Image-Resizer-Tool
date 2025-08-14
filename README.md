## 🖼 Image Resizer Tool

A simple Python script using Pillow to resize images.
You can easily shrink or enlarge an image and save the resized version.

## 📌 Features

Opens any image using Pillow.

Prints the original and resized dimensions.

Saves the resized image to disk.

Works with JPEG, PNG, and other formats supported by Pillow.

## 🛠 Requirements

Make sure you have Python 3.x installed, and install Pillow:

pip install pillow

## 📂 Usage

Place your image (e.g., fuzi-san.jpeg) in the project folder.

Update the image path in the script (or modify it to take input from the user).

Run the script:

python "Image Resizer Tool.py"


## ⚠ Notes

.resize() creates a new image — it does not modify the original image in place.

Ensure the file path is correct, or use an absolute path to avoid FileNotFoundError.

You can change the resize factor from //3 to any other ratio.
