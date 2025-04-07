from datetime import datetime
class AttendanceModel:
    def mark_attendance(self,name):
        with open('C:/Mini Project(5)/Code/Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    time = now.strftime('%H:%M:%S')
                    date= datetime.today().date()
                    f.writelines(f'\n{name},{date},{time}')
                    return 