import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for
from bcrypt import checkpw
from models.employee_model import EmployeeModel
from models.attendance_model import AttendanceModel
from utils.face_utils import blink_detection
import cv2
import pandas as pd
import face_recognition
import numpy as np
import os
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

employee_model = EmployeeModel()
attendance_model = AttendanceModel()

path = 'C:/Mini Project(5)/Code/static/images'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login_post():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM admin WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and checkpw(password, result[0]):
            session["admin_logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template('invalid.html')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/emp')
def emp():
    employees = employee_model.get_all_employees()
    return render_template('emp.html', employees=employees)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form.get('employee_name')
        employee_id = request.form.get('employee_id')
        photo = request.files['employee_photo']
        employee_model.register_employee(name, employee_id, photo)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    data=pd.read_csv('C:/Mini Project(5)/Code/Attendance.csv')
    data_list = data.to_dict(orient='records')
    return render_template('attendance.html', data=data_list)
    

@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    if request.method == 'POST':
        encodeListKnown = findEncodings(images)

        video_capture = cv2.VideoCapture(0)
        blink_detected = False
        last_blink_time = time.time()
        while True:
            success,img = video_capture.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            blink,value=blink_detection(img)
            if blink and not blink_detected and (time.time() - last_blink_time > 2):
                for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]: 
                        name = classNames[matchIndex].upper()
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        attendance_model.mark_attendance(name)
                        return render_template('atd.html', name=name)
            elif not blink:
                blink_detected = False 
            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if not blink_detected:
            return value
            
    return render_template('mark_attendance.html')

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

if __name__ == '__main__':
    app.run(debug=True)