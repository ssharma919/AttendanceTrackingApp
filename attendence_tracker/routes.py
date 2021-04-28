from flask import render_template, url_for, request, flash, redirect, session
from attendence_tracker import app, db, bcrypt
from attendence_tracker.forms import LoginForm
from attendence_tracker.models import Student, Teacher, Course
from flask_login import login_user, current_user, logout_user


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
                login_user(student, radio)
                return redirect(url_for('student_dashboard'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        elif radio == 'Teacher':
            teacher = Teacher.query.filter_by(
                username=form.username.data).first()
            if teacher and bcrypt.check_password_hash(teacher.password, form.password.data):
                login_user(teacher, radio)
                return redirect(url_for('student_dashboard'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/student-dashboard')
def student_dashboard():
    print(current_user)
    print(Course.query.all())
    return render_template('teststudent.html', current_user=current_user)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
