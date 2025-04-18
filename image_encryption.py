from PIL import Image

# This function shifts the pixel color values by a given value
def shift_pixel(value, shift):
    return (value + shift) % 256  # Using modulo ensures values stay within the 0-255 range

def reverse_shift_pixel(value, shift):
    return (value - shift) % 256

# Encrypts the image by applying the shift to each pixel
def encrypt_image(image_path, shift):
    img = Image.open(image_path)
    pixels = img.load()  # Access the pixel data
    width, height = img.size
    mode = img.mode  # Get image mode (e.g., RGB, L)

    for i in range(width):
        for j in range(height):
            if mode == "RGB":
                r, g, b = pixels[i, j]
                # Shift each channel separately
                r = shift_pixel(r, shift)
                g = shift_pixel(g, shift)
                b = shift_pixel(b, shift)
                pixels[i, j] = (r, g, b)
            elif mode == "L":  # For grayscale images (mode "L")
                pixels[i, j] = shift_pixel(pixels[i, j], shift)

    encrypted_path = "encrypted_" + image_path.split("\\")[-1]
    img.save(encrypted_path)
    print(f"✅ Image encrypted and saved as {encrypted_path}")

# Decrypts the image by reversing the shift
def decrypt_image(image_path, shift):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    mode = img.mode

    for i in range(width):
        for j in range(height):
            if mode == "RGB":
                r, g, b = pixels[i, j]
                r = reverse_shift_pixel(r, shift)
                g = reverse_shift_pixel(g, shift)
                b = reverse_shift_pixel(b, shift)
                pixels[i, j] = (r, g, b)
            elif mode == "L":
                pixels[i, j] = reverse_shift_pixel(pixels[i, j], shift)

    decrypted_path = "decrypted_" + image_path.split("\\")[-1]
    img.save(decrypted_path)
    print(f"✅ Image decrypted and saved as {decrypted_path}")

def main():
    print("🔐 Welcome to Image Encryptor")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    path = input("Enter path of the image file (e.g., Sample.png): ").strip()
    shift = int(input("Enter shift value (try between 50 and 150): "))

    if choice == 'E':
        encrypt_image(path, shift)
    elif choice == 'D':
        decrypt_image(path, shift)
    else:
        print("❌ Invalid choice. Please type 'E' or 'D'.")

if __name__ == "__main__":
    main()
