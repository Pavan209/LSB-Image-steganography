 LSB Image Steganography

 - Overview
LSB (Least Significant Bit) Image Steganography is a technique for hiding secret messages within digital images by altering the least significant bits of their pixel values. This project implements a Pythonbased tool to encode and decode messages in images, ensuring secure communication.


 - Features
 Message Encoding: Hide secret messages in images using the LSB technique.
 Message Decoding: Extract hidden messages from stego images.
 Encryption Key Support: Enhance security with a numeric encryption key to control the embedding location.
 Flexible Input: Userfriendly input for encoding and decoding operations.


- How It Works:

 Encoding:
1. The secret message is converted into a binary format.
2. The binary message is embedded into the least significant bits of the image's pixel values.
3. A delimiter (`1111111111111110`) is added at the end of the message to signal the termination.

 Decoding:
1. The embedded binary data is extracted from the least significant bits of the image.
2. The binary data is read until the delimiter is detected.
3. The binary data is converted back to readable text.


 - Features of the LSB Method
 Security: Messages are hidden in a way that is imperceptible to the human eye.
 Simplicity: Efficient and easytouse encoding and decoding process.
 Compatibility: Suitable for lossless image formats like PNG, ensuring the integrity of the hidden message.


 - Limitations
 Only supports lossless image formats (e.g., PNG).
 Message size is limited by the number of pixels in the image.
 Altering the stego image (e.g., compression, resizing) may damage the hidden message.


 - Applications
 Secure Communication: Send confidential messages hidden within images.
 Watermarking: Embed metadata or ownership information into digital images.
 Forensics: Conceal critical information for investigative purposes.


 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.



 - Acknowledgments
 The project utilizes the Pillow library for image processing and NumPy for efficient data manipulation.
 Inspired by the growing demand for secure and creative data hiding techniques.

