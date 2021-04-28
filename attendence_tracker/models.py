from attendence_tracker import db, login_manager, bcrypt
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

    student = db.relationship('Student', viewonly=True)
    teacher = db.relationship('Teacher', viewonly=True)
    name = db.Column(db.String(30), nullable=False)
    student_attendence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Courses('{self.name}', '{self.student}', '{self.teacher}', '{self.student_attendence}')"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course')

    def __repr__(self):
        return f"Student('{self.name}')"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course')

    def __repr__(self):
        return f"Teacher('{self.name}')"


def populate_db():
    s1 = Student(name='Anthony Yates', username='ayates',
                 password=bcrypt.generate_password_hash('denver').decode('utf-8'))
    s2 = Student(name='Stacy Mullen', username='smullen',
                 password=bcrypt.generate_password_hash('nuggets').decode('utf-8'))
    s3 = Student(name='George Weston', username='gweston',
                 password=bcrypt.generate_password_hash('joker').decode('utf-8'))
    db.session.add_all([s1, s2, s3])

    t1 = Teacher(name='Tegan Cary', username='tcary',
                 password=bcrypt.generate_password_hash('bluearrow').decode('utf-8'))
    t2 = Teacher(name='Chyna Wilkerson',
                 username='cwilkerson', password=bcrypt.generate_password_hash('basketball').decode('utf-8'))
    db.session.add_all([t1, t2])

    c1 = Course(student=s1.name, teacher=t1.name, name='Math')
    c2 = Course(student=s2.name, teacher=t1.name, name='Math')
    c3 = Course(student=s1.name, teacher=t2.name, name='CS')
    c4 = Course(student=s3.name, teacher=t2.name, name='CS')
    db.session.add_all([c1, c2, c3, c4])
    db.session.commit()
