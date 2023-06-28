import flask_wtf, wtforms
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




class AddUser():
    user_name = wtforms.StringField('user_name')
    street = wtforms.StringField('street')
    city = wtforms.StringField('city')
    zipcode = wtforms.StringField('zipcode')
    submit = wtforms.SubmitField('Save')




