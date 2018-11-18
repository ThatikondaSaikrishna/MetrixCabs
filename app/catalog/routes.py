from app.catalog import main

from app import db

from app.catalog.models import EmpDetails , EmpIds

from app.auth.models import EmpDetails

from flask_login import login_user , logout_user , login_required , current_user

from flask import render_template,request , flash , redirect , url_for

from flask import render_template

from app.catalog.forms import EditDetailsForm , CreateBookForm

from app.auth.send_email import send_email

from app.auth.send_manager_email import send_manager_email

from datetime import datetime,time

from app.auth.forms import EmpLogHistory

#from app.auth.models import EmpLogoutHistory

@main.route('/')
def display_books():
    empdetail = EmpDetails.query.all()
    return render_template('home.html', empdetail=empdetail)

@main.route('/sorry')
def display_books1():
    empdetail = EmpDetails.query.all()
    return render_template('home1.html', empdetail=empdetail)

@main.route('/edit/details/<book_id>', methods=['GET','POST'])
@login_required

def edit_details(book_id):

    empdetails = EmpDetails.query.filter_by(emp_id=book_id).first()
    #logout=empdetails.emp_logout
    now = datetime.now()
    now1 = now.strftime("%X")
    logout = str(empdetails.emp_logout)
    if logout=='22:00:00':
        print(now1)
        print(logout)
        time1='21:35:00'
        time2='23:00:00'
        print(time1)
        if now1>time1 and now1<time2:
            print(now)
            print(empdetails.emp_logout)
            flash('Sorry... you have to edit your details atleat 25mins before your logout. Please reachout your manager for any assistance.')
            return redirect(url_for('main.display_books1'))
        else:
            form = EditDetailsForm(obj=empdetails)
            if form.validate_on_submit():
                empdetails.emp_name = form.emp_name.data
                empdetails.emp_login = form.emp_login.data
                empdetails.emp_logout = form.emp_logout.data
                print(empdetails.emp_logout)
                print(type(str(empdetails.emp_logout)))

                    # SP-PI Team
                if empdetails.emp_id==20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782 :
                    send_manager_email(empdetails.emp_logout,empdetails.emp_name,manager_email="thatikondasaikrishna111@gmail.com")
                else:
                    send_manager_email(empdetails.emp_logout, empdetails.emp_name,empdetails.emp_login,manager_email="krishnakrrish888@gmail.com",name="sreenath Velaga")
                send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

                db.session.add(empdetails)
                db.session.commit()
                flash('Details Edited Successfully')
                return redirect(url_for('main.display_books'))
            return render_template('editdetails.html', form=form)
    elif logout=='12:00:00':
        print(now1)
        print(logout)
        time1 = '23:35:00'
        time2='01:00:00'
        print(time1)
        if now1 > time1 and now1 < time2:
            print(now)
            print(empdetails.emp_logout)
            flash('Sorry... you have to edit your details atleat 25mins before your logout. Please reachout your manager for any assistance.')
            return redirect(url_for('main.display_books1'))
        else:
            form = EditDetailsForm(obj=empdetails)
            if form.validate_on_submit():
                empdetails.emp_name = form.emp_name.data
                empdetails.emp_login = form.emp_login.data
                empdetails.emp_logout = form.emp_logout.data
                print(empdetails.emp_logout)
                print(type(str(empdetails.emp_logout)))
                    # SP-PI Team
                if empdetails.emp_id==20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782 :
                    send_manager_email(empdetails.emp_logout,empdetails.emp_name,manager_email="thatikondasaikrishna111@gmail.com")
                else:
                    send_manager_email(empdetails.emp_logout, empdetails.emp_name,empdetails.emp_login,manager_email="krishnakrrish888@gmail.com",name="sreenath Velaga")
                send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

                db.session.add(empdetails)
                db.session.commit()
                flash('Details Edited Successfully')
                return redirect(url_for('main.display_books'))
            return render_template('editdetails.html', form=form)
    elif logout=='02:00:00':
        print(now1)
        print(logout)
        time1 = '01:35:00'
        time2='03:00:00'
        print(time1)
        if now1 > time1 and now1 < time2:
            print(now)
            print(empdetails.emp_logout)
            flash('Sorry... you have to edit your details atleat 25mins before your logout. Please reachout your manager for any assistance.')
            return redirect(url_for('main.display_books1'))
        else:
            form = EditDetailsForm(obj=empdetails)
            if form.validate_on_submit():
                empdetails.emp_name = form.emp_name.data
                empdetails.emp_login = form.emp_login.data
                empdetails.emp_logout = form.emp_logout.data
                print(empdetails.emp_logout)
                print(type(str(empdetails.emp_logout)))
                    # SP-PI Team
                if empdetails.emp_id==20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782 :
                    send_manager_email(empdetails.emp_logout,empdetails.emp_name,manager_email="thatikondasaikrishna111@gmail.com")
                else:
                    send_manager_email(empdetails.emp_logout, empdetails.emp_name,empdetails.emp_login,manager_email="krishnakrrish888@gmail.com",name="sreenath Velaga")
                send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

                db.session.add(empdetails)
                db.session.commit()
                flash('Details Edited Successfully')
                return redirect(url_for('main.display_books'))
            return render_template('editdetails.html', form=form)
    elif logout=='04:00:00':
        print(now1)
        print(logout)
        time1 = '03:35:00'
        time2='5:00:00'
        print(time1)
        if now1 > time1 and now1 < time2:
            print(now)
            print(empdetails.emp_logout)
            flash('Sorry... you have to edit your details atleat 25mins before your logout. Please reachout your manager for any assistance.')
            return redirect(url_for('main.display_books1'))
        else:
            form = EditDetailsForm(obj=empdetails)
            if form.validate_on_submit():
                empdetails.emp_name = form.emp_name.data
                empdetails.emp_login = form.emp_login.data
                empdetails.emp_logout = form.emp_logout.data
                print(empdetails.emp_logout)
                print(type(str(empdetails.emp_logout)))
                    # SP-PI Team
                if empdetails.emp_id==20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782 :
                    send_manager_email(empdetails.emp_logout,empdetails.emp_name,manager_email="thatikondasaikrishna111@gmail.com")
                else:
                    send_manager_email(empdetails.emp_logout, empdetails.emp_name,empdetails.emp_login,manager_email="krishnakrrish888@gmail.com",name="sreenath Velaga")
                send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

                db.session.add(empdetails)
                db.session.commit()
                flash('Details Edited Successfully')
                return redirect(url_for('main.display_books'))
            return render_template('editdetails.html', form=form)
    elif logout=='06:00:00':
        print(now1)
        print(logout)
        time1  = '04:35:00'
        time2 ='07:00:00'
        print(time1)
        if now1 > time1 and now1 < time2:
            print(now)
            print(empdetails.emp_logout)
            flash('Sorry... you have to edit your details atleat 25mins before your logout. Please reachout your manager for any assistance.')
            return redirect(url_for('main.display_books1'))
        else:
            form = EditDetailsForm(obj=empdetails)
            if form.validate_on_submit():
                empdetails.emp_name = form.emp_name.data
                empdetails.emp_login = form.emp_login.data
                empdetails.emp_logout = form.emp_logout.data
                print(empdetails.emp_logout)
                print(type(str(empdetails.emp_logout)))
                    # SP-PI Team
                if empdetails.emp_id==20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782 :
                    send_manager_email(empdetails.emp_logout,empdetails.emp_name,manager_email="thatikondasaikrishna111@gmail.com")
                else:
                    send_manager_email(empdetails.emp_logout, empdetails.emp_name,empdetails.emp_login,manager_email="krishnakrrish888@gmail.com",name="sreenath Velaga")
                send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

                db.session.add(empdetails)
                db.session.commit()
                flash('Details Edited Successfully')
                return redirect(url_for('main.display_books'))
            return render_template('editdetails.html', form=form)
    else:
        flash('Sorry we dont provide cabs for '+str(empdetails.emp_logout)+' logout.Please check with you manager')
        return redirect(url_for('main.display_books1'))

####### Edit after 2 monts #######

@main.route('/edit/details/shiftchange/<book_id>', methods=['GET','POST'])
@login_required

def edit_details_shiftchange(book_id):
    empdetails = EmpDetails.query.filter_by(emp_id=book_id).first()
    form = EditDetailsForm(obj=empdetails)
    if form.validate_on_submit():
        empdetails.emp_name = form.emp_name.data
        empdetails.emp_login = form.emp_login.data
        empdetails.emp_logout = form.emp_logout.data
        print(empdetails.emp_logout)
        print(type(str(empdetails.emp_logout)))
        # SP-PI Team
        if empdetails.emp_id == 20786 | 20661 | 20813 | 20651 | 20853 | 20833 | 20631 | 20695 | 20661 | 20812 | 20761 | 20770 | 20783 | 20782:
            send_manager_email(empdetails.emp_logout, empdetails.emp_name,
                               manager_email="thatikondasaikrishna111@gmail.com")
        else:
            send_manager_email(empdetails.emp_logout, empdetails.emp_name, empdetails.emp_login,
                               manager_email="krishnakrrish888@gmail.com", name="sreenath Velaga")
        send_email(empdetails.emp_email, empdetails.emp_name, empdetails.emp_logout)

        db.session.add(empdetails)
        db.session.commit()
        flash('Shift change has been updated Successfully')
        return redirect(url_for('main.display_books'))
    return render_template('editdetails.html', form=form)


