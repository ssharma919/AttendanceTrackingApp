from flask import render_template, url_for, request, flash, redirect, session
from attendance_tracker import app, db, bcrypt
from attendance_tracker.forms import LoginForm
from attendance_tracker.models import Student, Teacher, Course
from flask_login import login_user, current_user, logout_user
from datetime import date


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('student_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        radio = request.form.get('btnradio')
        session['radio'] = radio
        if radio == 'Student':
            student = Student.query.filter_by(
                username=form.username.data).first()
            if student and bcrypt.check_password_hash(student.password, form.password.data):
                login_user(student)
                return redirect(url_for('student_dashboard'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        elif radio == 'Teacher':
            teacher = Teacher.query.filter_by(
                username=form.username.data).first()
            if teacher and bcrypt.check_password_hash(teacher.password, form.password.data):
                login_user(teacher)
                return redirect(url_for('teacher_dashboard'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/student-dashboard', methods=['GET', 'POST'])
def student_dashboard():
    if request.method == 'POST':
        checks = request.form.getlist('attend_check')
        for course_name in checks:
            c = Course.query.filter_by(
                name=course_name, student=current_user).first()
            c.student_attendance += 1
            print(c.student_attendance)
            c.last_log = date.today()
            db.session.commit()
    return render_template('student_dashboard.html', current_user=current_user, date=date.today, round=round, min=min)


@app.route('/teacher-dashboard', methods=['GET', 'POST'])
def teacher_dashboard():
    if request.method == 'POST':
        return redirect(url_for('course_breakdown', course_name=request.form['breakdown']))
    course_set = set()
    for c in current_user.courses:
        course_set.add(c.name)
    course_list = []
    for c_name in course_set:
        attendance = 0
        start_date = Course.query.filter_by(
            name=c_name, teacher=current_user).first().start_date
        for c in Course.query.filter_by(name=c_name, teacher=current_user).all():
            attendance += c.student_attendance
        attendance = round(attendance / (((date.today() - start_date).days) * len(
            Course.query.filter_by(name=c_name, teacher=current_user).all())) * 100)
        course_list.append((c_name, min(attendance, 100)))
    return render_template('teacher_dashboard.html', current_user=current_user, date=date.today, course_list=course_list)


@app.route('/course-breakdown')
def course_breakdown():
    course_name = request.args.get('course_name')
    course_list = Course.query.filter_by(
        name=course_name, teacher=current_user).all()
    days = (date.today() - course_list[0].start_date).days
    return render_template('course_breakdown.html', course_name=course_name, course_list=enumerate(course_list), days=days, round=round, date=date.today, min=min)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
