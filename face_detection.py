import dlib
import cv2

# Load the face detector
detector = dlib.get_frontal_face_detector()

# Load an image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = detector(gray)

# Print the number of faces detected
print("Number of faces detected: {}".format(len(faces)))
