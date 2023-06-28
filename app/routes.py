from flask import Flask, render_template
from app import app, db
from app.models import User
from .forms import AddUser

@app.route('/', methods=['GET', 'POST'])
def index():
    def filtre0():
        user = User.query.all()
        return user

    def filtre1():
        city = "Roscoeview"
        user = User.query.filter(User.address.city == city).all()
        return user
    
    def filtre2():
        user = User.query.limit(5).all()
        return user

    def filtre3():
        user = User.query.filter(User.address.zipcode.like('5%')).all()
        return user
    
    result0 = filtre0()
    result1 = filtre1()
    result2 = filtre2()
    result3 = filtre3()

    return render_template('home.html', result0=result0, result1=result1, result2=result2 ,result3=result3)


@app.route('/add_user')
def add_user():
    form = AddUser
    if form.validate_on_submit():
        user_name = form.user_name.data,
        street = form. street.data,
        city = form.city.data,
        zipcode = form.zipcode.data,
        submit = form. submit.data

        add_user = AddUser(user_name=user_name,street=street,city=city, zipcode=zipcode) 

        db.session.add(add_user)
        db.session.commit()
        return('Succces')
    return render_template('add_user.html', form=form)