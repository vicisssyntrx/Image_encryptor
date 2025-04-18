# PixelEncryptor

A simple image encryption and decryption tool using pixel manipulation in Python.

## Features

- Encrypts images by manipulating RGB pixel values.
- Decrypts to the original image using reverse operations.
- Uses basic math on each pixel.
- CLI-based and beginner friendly.

## How It Works

Each pixel's RGB values are altered using a mathematical operation (e.g., addition or XOR with a secret key). The reverse of that operation is used to decrypt.

## Requirements

- Python 3
- Pillow (`pip install Pillow`)

## Usage

```bash
python image_encryption.py
