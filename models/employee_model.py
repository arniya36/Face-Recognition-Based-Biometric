import sqlite3
class EmployeeModel:
    def __init__(self):
        self.conn = sqlite3.connect('attendance.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employees (
            Eid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            photo_path TEXT NOT NULL
        )
        '''
        self.conn.execute(query)

    def register_employee(self, name, employee_id, photo):
        photo_path = f'C:/Mini Project(5)/Code/static/images/{employee_id}.jpg'
        photo.save(photo_path)
        query = 'INSERT INTO employees (Eid, name, photo_path) VALUES (?, ?, ?)'
        self.conn.execute(query, (employee_id, name, photo_path))
        self.conn.commit()

    def get_all_employees(self):
        query = 'SELECT * FROM employees'
        return self.conn.execute(query).fetchall()
