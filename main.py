import os
import face_recognition
import shutil

# Capture a new photo and save it in the "pictures" folder
os.system("raspistill -o pictures/new_photo.jpg")

# Detect faces in the new photo
new_image = face_recognition.load_image_file("pictures/new_photo.jpg")
new_face_locations = face_recognition.face_locations(new_image)
new_face_encodings = face_recognition.face_encodings(new_image, new_face_locations)

# Compare the detected faces with known faces in the "pictures" folder
known_faces = []
known_face_encodings = []
for filename in os.listdir("pictures"):
    if filename.endswith(".jpg"):
        image = face_recognition.load_image_file("pictures/" + filename)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        if len(face_encodings) > 0:
            known_faces.append(filename)
            known_face_encodings.append(face_encodings[0])

# Group similar photos based on recognized faces
face_distances = face_recognition.face_distance(known_face_encodings, new_face_encodings[0])
matches = face_recognition.compare_faces(known_face_encodings, new_face_encodings[0])
distances = zip(face_distances, matches, known_faces)
distances = sorted(distances)

# Create a new folder for each group of similar photos and copy them
if not os.path.exists("groups"):
    os.mkdir("groups")
for i, (distance, match, filename) in enumerate(distances):
    if match and distance < 0.6:
        group_folder = "groups/group_" + str(i)
        os.mkdir(group_folder)
        shutil.copy("pictures/" + filename, group_folder)
        shutil.copy("pictures/new_photo.jpg", group_folder)