# Face Recognition-Based Biometric

This project is a complete Employee Attendance and Management System built using Python. It uses face recognition and blink detection to authenticate employees. The system includes user registration, admin access, and a secure attendance marking mechanism.

## Features

- Face Recognition using OpenCV and dlib
- Blink Detection to avoid spoofing (via Eye Aspect Ratio)
- Admin login protected using bcrypt password hashing
- New Employee Registration
- Attendance Recording with date and time
- SQLite Database for persistent storage
- Flask-based UI with separate views for admin and employee
- Clear separation of models, templates, and static files

## Tech Stack

- Python
- OpenCV
- dlib
- face_recognition
- Flask
- SQLite
- bcrypt

## Project Structure

Employee-Attendance-System/
├── app.py                         # Main Flask application
├── templates/                     # HTML templates
│   ├── login.html
│   ├── dashboard.html
│   ├── register.html
│   ├── attendance.html
│   └── ...
├── static/                        # Static files (CSS, JS, images)
│   └── css/
│       ├── login.css
│       ├── dashboard.css
│       └── ...
├── models/                        # Business logic and model handlers
│   ├── attendance_model.py
│   ├── employee_model.py
|   ├── shape_predictor_68_face_landmarks.dat   # Required by dlib (Too large for GitHub)
│   └── mmod_human_face_detector.dat
├── database/
│   └── attendance.db              # SQLite database
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
└── ...

## Future Improvements

- Add email or SMS notifications
- Generate attendance reports in PDF/Excel format
- Add logging and monitoring
- Deploy the app using Docker or to a cloud platform
