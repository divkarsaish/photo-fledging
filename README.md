# photo-fledging

Facial Recognition Grouping Algorithm
Introduction
In this article, we will explore a Python code snippet that utilizes the face_recognition library to capture and group similar photos based on recognized faces. The code captures a new photo, detects faces in it, compares them with known faces, and creates a new folder for each group of similar photos.

Key Concepts
Before diving into the code, let's understand some key concepts:

Facial Recognition: Facial recognition is a technology that identifies or verifies a person's identity by analyzing and comparing patterns in their facial features.

Face Encoding: Face encoding is the process of extracting unique numerical representations, or encodings, from facial images. These encodings are used to compare and match faces.

Face Location: Face location refers to the coordinates of the bounding box that surrounds a detected face in an image.

Face Distance: Face distance is a numerical value that represents the similarity or dissimilarity between two face encodings. A lower distance indicates a higher similarity.

Code Structure
The code snippet provided can be divided into the following sections:

Capture a New Photo: The code uses the os.system function to capture a new photo using the Raspberry Pi camera module and save it in the "pictures" folder.

Detect Faces in the New Photo: The code loads the new photo and uses the face_recognition library to detect faces in it. It retrieves the face locations and encodings.

Compare with Known Faces: The code iterates through the images in the "pictures" folder and compares the detected faces with the known faces. It stores the known faces' filenames and encodings in separate lists.

Group Similar Photos: The code calculates the face distances between the new face encodings and the known face encodings. It then compares the face distances with a threshold value (0.6) to determine if the faces are similar. The similar photos are sorted based on their distances.

Create New Folders and Copy Photos: The code creates a new folder for each group of similar photos in the "groups" directory. It copies the similar photos and the new photo into their respective group folders.

To run install face_recognition and give specific paths 
