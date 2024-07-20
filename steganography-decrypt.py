import cv2
import hashlib

# Specify the path to the encrypted image
encrypted_image_path = r"encryptedImage.jpg"

# Read the encrypted image
img = cv2.imread(encrypted_image_path)

# Check if the image is successfully loaded
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
height, width, channels = img.shape

# Prompt the user to input the password
password = input("Enter the passcode: ")

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()



import cv2
import hashlib

# Specify the path to the encrypted image
encrypted_image_path = r"encryptedImage.jpg"

# Read the encrypted image
img = cv2.imread(encrypted_image_path)

# Check if the image is successfully loaded
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
height, width, channels = img.shape

# Prompt the user to input the password
password = input("Enter the passcode: ")

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()

# Initialize variables for image coordinates and color channel
n = 0  # Row index
m = 0  # Column index
z = 0  # Color channel index

# Initialize the decrypted message
decrypted_msg = ""

# Decode the secret message from the image using the hashed password
while True:
    # Calculate the original character
    original_value = (int(img[n, m, z]) - hashed_password[len(decrypted_msg) % len(hashed_password)]) % 256
    decrypted_char = chr(original_value)
    
    # Check for the terminator character
    if decrypted_char == chr(0):
        break
    
    # Add the decrypted character to the message
    decrypted_msg += decrypted_char
    
    # Move to the next pixel
    m += 1
    
    # If the column index exceeds the image width, reset it and move to the next row
    if m >= width:
        m = 0
        n += 1
    
    # If the row index exceeds the image height, stop decoding (reached end of image)
    if n >= height:
        break
    
    # Cycle through the color channels (0, 1, 2) for RGB
    z = (z + 1) % 3

print(f"The decrypted message is: {decrypted_msg}")

