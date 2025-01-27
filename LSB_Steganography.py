from PIL import Image
import numpy as np


def encode_message_in_image(image_path, message, output_path, key):
    """Encode a message into an image using LSB steganography."""
    image = Image.open(image_path)
    image_data = np.array(image)
    flat_image_data = image_data.flatten()
    
    # Convert the message to binary and include a delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'
    
    if len(binary_message) > len(flat_image_data):
        raise ValueError("Message is too large to fit in the image!")
    
    # Use the key to determine the starting point
    start = int(key) % len(flat_image_data)
    
    # Embed the binary message in the least significant bits
    for i, bit in enumerate(binary_message):
        flat_image_data[start + i] = (flat_image_data[start + i] & ~1) | int(bit)
    
    # Reshape the data back to the original image dimensions
    encoded_image_data = flat_image_data.reshape(image_data.shape)
    encoded_image = Image.fromarray(encoded_image_data.astype(np.uint8))
    encoded_image.save(output_path)
    print(f"Message encoded successfully into {output_path}")


def decode_message_from_image(image_path, key):
    """Decode a message from an image using LSB steganography."""
    image = Image.open(image_path)
    image_data = np.array(image)
    flat_image_data = image_data.flatten()
    
    # Use the key to determine the starting point
    start = int(key) % len(flat_image_data)
    
    binary_message = []
    for i in range(start, len(flat_image_data)):
        binary_message.append(flat_image_data[i] & 1)
        if binary_message[-16:] == [1] * 15 + [0]: # Check for delimiter
            break
    
    binary_message = binary_message[:-16] # Remove the delimiter
    decoded_message = ''.join(chr(int(''.join(map(str, binary_message[i:i + 8])), 2)) for i in range(0, len(binary_message), 8))
    print(f"Decoded Message: {decoded_message}")
    return decoded_message


if __name__ == "__main__":
    print("Welcome to LSB Image Steganography!")
    print("1. Encode")
    print("2. Decode")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        input_image = input("Enter the path of the input image (e.g., input_image.png): ")
        secret_message = input("Enter the secret message to encode: ")
        output_image = input("Enter the path to save the output stego image (e.g., output_image.png): ")
        key = input("Enter an encryption key (numeric): ")
        
        try:
            encode_message_in_image(input_image, secret_message, output_image, key)
        except Exception as e:
            print(f"Error: {e}")
    
    elif choice == "2":
        input_image = input("Enter the path of the stego image (e.g., output_image.png): ")
        key = input("Enter the decryption key (numeric): ")
        
        try:
            decode_message_from_image(input_image, key)
        except Exception as e:
            print(f"Error: {e}")
    
    else:
        print("Invalid choice. Please run the program again.")