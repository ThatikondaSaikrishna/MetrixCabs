from flask import render_template,request , flash , redirect , url_for

from flask import Flask, render_template, request, send_file,send_from_directory

from flask_login import login_user , logout_user , login_required , current_user

from app.auth.forms import RegistrationForm , LoginForm  , CreateBookForm

from app.auth import authentication as at

from app.auth.send_email import send_email

from app import db

from app.catalog import main

from app.auth.models import EmpDetails , EmpIdscheck

import pandas as pd

from sqlalchemy import create_engine

import datetime

import re

@at.route('/register' , methods=['GET','POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    if form.validate_on_submit():
       EmpDetails.create_user(
           empid=form.empid.data,
           name=form.name.data,
           email=form.email.data,
           gender=form.gender.data,
           login=form.login.data,
           logout=form.logout.data,
           password=form.password.data,
           confirm=form.confirm.data,
           hno=form.hno.data,
           address=form.address.data,
           pincode=form.pincode.data )
       flash('Registration Successful')
       return redirect(url_for('authentication.do_the_login'))

    return render_template('registration.html',form=form)


@at.route('/login', methods=['GET','POST'])
def do_the_login():

    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))

    form=LoginForm()

    if form.validate_on_submit():
        empdetails=EmpDetails.query.filter_by(emp_id=form.empid.data).first()
        if not empdetails or not empdetails.check_password(form.password.data):
            flash('Invalid Credentials , Please try again')
            return redirect(url_for('authentication.do_the_login'))
        login_user(empdetails,form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html',form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))


@at.route('/details/<emp>',methods=['GET','POST'])
@login_required
def details_user(emp):
    empdetails = EmpDetails.query.all()
    print(emp)
    if str(emp)=='10786':
        return render_template('table.html', empdetails=empdetails)
    else:
        flash('Sorry you cant see this tab. This will be used by Admin Team.')
        return redirect(url_for('main.display_books1'))


@at.route('/profile')
@login_required
def profile_user():
    if current_user.is_authenticated:
        return render_template('profile.html')

@at.route('/table/<logout>',methods=['GET','POST'])
@login_required
def logout_emps(logout):
    global filename
    empdetails = EmpDetails.query.all()
    print("start table function")
    engine = create_engine('postgresql://postgres:postgres1826@localhost/height_collector')
    if logout == '22:00:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='22:00:00' order by emp_id asc  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '22:30:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='22:30:00'  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '12:00:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='12:00:00'  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '12:30:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='12:30:00'  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '02:00:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='02:00:00'  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '02:30:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='02:30:00'  '''
        df = pd.read_sql_query(query, engine)
    elif logout == '04:00:00':
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='04:00:00' order by emp_id asc '''
        df = pd.read_sql_query(query, engine)
    else:
        query = ''' select emp_id , emp_name,emp_logout,emp_address from empdetails where emp_logout='04:30:00'  '''
        df = pd.read_sql_query(query, engine)
    #filename = datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f" + ".xlsx")
    filename = "app/auth/sample_files.csv"
    df.to_csv(filename,index=True)
    if current_user.is_authenticated:
        return render_template("table.html", empdetails=empdetails,logout=logout, btn='download.html')


@at.route("/download-file/")
def download():
    #filename1=str(filename)
    filename = "app/auth/sample_files/some.csv"
    pattern = r"app/"
    filename2 = re.sub(pattern, "", filename)
    #print(filename1)
    #print(type(filename1))
    return send_file(filename2, attachment_filename='yourfile.csv', as_attachment=True)

@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


