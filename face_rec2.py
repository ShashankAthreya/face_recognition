import face_recognition
import os
import cv2


Testing_Data = "Testing_Data"
Training_Data = "Training_Data"
Tolerence = 0.6
Frame_thickness = 3
Font_thickness = 2
Model = "cnn" #or hog

print("Accesing known faces in training data")
known_faces = []
known_names = []

for name in os.listdir(Training_Data):
	for filename in os.listdir(f"{Training_Data}/{name}"):
		image = face_recognition.load_image_file(f"{Training_Data}/{name}/{filename}")
		encoding = face_recognition.face_encodings(image)
		known_faces.append(encoding)
		known_names.append(name)

print("Starting Testing for unknown faces")
for filename in os.listdir(Testing_Data):
	image = face_recognition.load_image_file(f"{Testing_Data}/{filename}")
	locations = face_recognition.face_locations(image,model=Model)
	encodings = face_recognition.face_encodings(image,locations)
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	for face_encoding, face_location in zip(encodings, locations):
		results = face_recognition.compare_faces([known_faces], face_encoding, Tolerence)
		match = None
		if True in results:
			match = known_names[results.index(True)]
			print(F"Match found: {match}")
			top_left = (face_location[3], face_location[0])
			bottom_right = (face_location[1], face_location[2])
			color = [0,255,0]
			cv2.rectangle(image, top_left, bottom_right, color, Frame_thickness)
			top_left = (face_location[3], face_location[2])
			bottom_right = (face_location[1], face_location[2]+22)
			cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
			cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), Font_thickness)

	cv2.imshow(filename, image)
	if cv2.waitKey(1) == ord('q'):
		break