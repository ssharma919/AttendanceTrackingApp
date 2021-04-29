from datetime import date
from attendance_tracker import db, login_manager, bcrypt
from flask import session
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    if session['radio'] == 'Student':
        return Student.query.get(int(user_id))
    else:
        return Teacher.query.get(int(user_id))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    student = db.relationship('Student')
    teacher = db.relationship('Teacher')
    name = db.Column(db.String(30), nullable=False)
    student_attendance = db.Column(db.Integer, default=0)
    start_date = db.Column(db.Date, default=date.today)
    last_log = db.Column(db.Date, default=date(2000, 1, 1))

    def __repr__(self):
        return f"Courses('{self.name}', '{self.student}', '{self.teacher}', '{self.student_attendance}')"


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course')

    def __repr__(self):
        return f"Student('{self.name}')"


class Teacher(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course')

    def __repr__(self):
        return f"Teacher('{self.name}')"
