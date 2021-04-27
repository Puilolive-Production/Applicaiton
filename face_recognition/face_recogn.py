import face_recognition
import cv2
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

# # Get a reference to webcam #0 (the default one)
# video_capture = cv2.VideoCapture(0)

known_face_encodings = []
known_face_names = []

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

def init_faces():
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("face_recognition/obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(new_image)[0]
    biden_image = face_recognition.load_image_file("face_recognition/biden.jpg")
    biden_face_encoding = face_recognition.face_encodings(new_image)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding
    ]
    known_face_names = [
        "Barack Obama",
        "Joe Biden"
    ]

def input_faces(user_name):
    # Define a video capture object
    vid = cv2.VideoCapture('http://192.168.0.173:4747/mjpegfeed?640x480')
    frame_set = []
    start_time = time.time()
    path = 'face_recognition/known-pics'
    while(True):
        # Capture the video frame by frame
        ret, frame = vid.read()
        # # Display the resulting frame
        # cv2.imshow('frame', frame)
        if time.time() - start_time >= 3: # <-- Check if 5 sec passed
            img_name = os.path.join(path, "{}.png".format(user_name))
            print(img_name)
            if frame is not None:
                cv2.imwrite(img_name, frame)
                print("{} written!".format(user_name))
                break
            else:
                print('Error: frame is none')
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    # Load a sample picture and learn how to recognize it.
    new_image = face_recognition.load_image_file("face_recognition/{}.jpg".user_name)
    new_face_encoding = face_recognition.face_encodings(new_image)[0]
    known_face_encodings.append(new_face_encoding)
    known_face_names.append(user_name)

def face_recogn(user_name):
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]


        process_this_frame = not process_this_frame

        # Hit 'q' on the keyboard to quit!
        if matches:
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
    return name

