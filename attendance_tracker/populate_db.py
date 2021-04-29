from datetime import date
from attendance_tracker import db, bcrypt
from attendance_tracker.models import Student, Teacher, Course


def populate_db():

    # Students

    s1 = Student(name='Anthony Yates', username='ayates',
                 password=bcrypt.generate_password_hash('denver').decode('utf-8'))
    s2 = Student(name='Stacy Mullen', username='smullen',
                 password=bcrypt.generate_password_hash('nuggets').decode('utf-8'))
    s3 = Student(name='George Weston', username='gweston',
                 password=bcrypt.generate_password_hash('joker').decode('utf-8'))
    s4 = Student(name='Walter Nelson', username='wnelson',
                 password=bcrypt.generate_password_hash('tiger').decode('utf-8'))
    s5 = Student(name='Ralph Diaz', username='rdiaz',
                 password=bcrypt.generate_password_hash('planet').decode('utf-8'))
    s6 = Student(name='Amy Parker', username='aparker',
                 password=bcrypt.generate_password_hash('comet').decode('utf-8'))
    s7 = Student(name='Ruth Barnes', username='rbarnes',
                 password=bcrypt.generate_password_hash('blackhole').decode('utf-8'))
    s8 = Student(name='Kenneth Bailey', username='kbailey',
                 password=bcrypt.generate_password_hash('buzzbuzz').decode('utf-8'))
    s9 = Student(name='Andrea Perez', username='aperez',
                 password=bcrypt.generate_password_hash('lunar').decode('utf-8'))
    s10 = Student(name='Douglas Green', username='dgreen',
                  password=bcrypt.generate_password_hash('eclipse').decode('utf-8'))
    s11 = Student(name='Martha Simmons', username='msimmons',
                  password=bcrypt.generate_password_hash('life42').decode('utf-8'))
    s12 = Student(name='Sarah Brooks', username='sbrooks',
                  password=bcrypt.generate_password_hash('binary').decode('utf-8'))

    db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])

    # Teachers

    t1 = Teacher(name='Tegan Cary', username='tcary',
                 password=bcrypt.generate_password_hash('bluearrow').decode('utf-8'))
    t2 = Teacher(name='Chyna Wilkerson', username='cwilkerson',
                 password=bcrypt.generate_password_hash('basketball').decode('utf-8'))
    t3 = Teacher(name='Chester Moore', username='cmoore',
                 password=bcrypt.generate_password_hash('emerald').decode('utf-8'))

    db.session.add_all([t1, t2, t3])

    # Student-Teacher-Course Relationships

    d = date(2021, 4, 14)

    c1 = Course(student=s1, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=14)
    c2 = Course(student=s2, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=12)
    c3 = Course(student=s4, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=10)
    c4 = Course(student=s5, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=13)
    c5 = Course(student=s7, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=11)
    c6 = Course(student=s8, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=8)
    c7 = Course(student=s9, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=14)
    c8 = Course(student=s10, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=12)
    c9 = Course(student=s11, teacher=t1, name='MATH 3215',
                start_date=d, student_attendance=14)
    c10 = Course(student=s12, teacher=t1, name='MATH 3215',
                 start_date=d, student_attendance=13)
    db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10])

    c1 = Course(student=s1, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=14)
    c2 = Course(student=s3, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=12)
    c3 = Course(student=s4, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=10)
    c4 = Course(student=s5, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=13)
    c5 = Course(student=s6, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=11)
    c6 = Course(student=s8, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=8)
    c7 = Course(student=s9, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=14)
    c8 = Course(student=s11, teacher=t1, name='CS 2051',
                start_date=d, student_attendance=12)
    db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])

    c1 = Course(student=s1, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=14)
    c2 = Course(student=s2, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=11)
    c3 = Course(student=s3, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=9)
    c4 = Course(student=s4, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=13)
    c5 = Course(student=s5, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=12)
    c6 = Course(student=s6, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=6)
    c7 = Course(student=s7, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=14)
    c8 = Course(student=s8, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=13)
    c9 = Course(student=s9, teacher=t2, name='ENGL 1102',
                start_date=d, student_attendance=12)
    c10 = Course(student=s10, teacher=t2, name='ENGL 1102',
                 start_date=d, student_attendance=13)
    c11 = Course(student=s11, teacher=t2, name='ENGL 1102',
                 start_date=d, student_attendance=14)
    c12 = Course(student=s12, teacher=t2, name='ENGL 1102',
                 start_date=d, student_attendance=13)
    db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])

    c1 = Course(student=s1, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=13)
    c2 = Course(student=s3, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=14)
    c3 = Course(student=s6, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=10)
    c4 = Course(student=s7, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=12)
    c5 = Course(student=s10, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=11)
    c6 = Course(student=s11, teacher=t3, name='AE 2202',
                start_date=d, student_attendance=10)
    db.session.add_all([c1, c2, c3, c4, c5, c6])

    c1 = Course(student=s1, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=13)
    c2 = Course(student=s2, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=14)
    c3 = Course(student=s4, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=10)
    c4 = Course(student=s8, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=12)
    c5 = Course(student=s10, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=11)
    c6 = Course(student=s12, teacher=t3, name='ECE 4280',
                start_date=d, student_attendance=10)
    db.session.add_all([c1, c2, c3, c4, c5, c6])

    c1 = Course(student=s1, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=13)
    c2 = Course(student=s2, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=14)
    c3 = Course(student=s5, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=10)
    c4 = Course(student=s7, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=12)
    c5 = Course(student=s9, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=11)
    c6 = Course(student=s11, teacher=t3, name='CS 4476',
                start_date=d, student_attendance=10)
    db.session.add_all([c1, c2, c3, c4, c5, c6])

    db.session.commit()
