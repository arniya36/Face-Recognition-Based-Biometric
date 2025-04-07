import cv2
import dlib
from scipy.spatial import distance

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Mini Project(5)/Code/models/shape_predictor_68_face_landmarks.dat")

LEFT_EYE = list(range(36, 42))
RIGHT_EYE = list(range(42, 48))

def calculate_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def blink_detection(frame):
    EAR_THRESHOLD = 0.2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        left_eye = [landmarks.part(i) for i in LEFT_EYE]
        right_eye = [landmarks.part(i) for i in RIGHT_EYE]
        left_eye_points = [(p.x, p.y) for p in left_eye]
        right_eye_points = [(p.x, p.y) for p in right_eye]
        left_ear = calculate_ear(left_eye_points)
        right_ear = calculate_ear(right_eye_points)
        avg_ear = (left_ear + right_ear) / 2
        if avg_ear < EAR_THRESHOLD:
            return True,None
    return False,'Detected proxy activity'