from ast import Str
from datetime import date
from flask.app import Flask
from sqlalchemy.orm import query
from wtforms.fields.core import DateField, DecimalField, IntegerField
from application.models import Customers, Materials, Tasks
from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, AnyOf, Email

class AddCustomerForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    home_num = StringField('Home Number:', validators=[DataRequired()])
    mobile_num = StringField('Mobile Number:', validators=[DataRequired()])
    address = StringField('Address:', validators=[DataRequired()])
    town_city = StringField('Town/City:', validators=[DataRequired()])
    county = StringField('County:', validators=[DataRequired()])
    postcode = StringField('Postcode:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddTaskForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    desc = StringField('Description:', validators=[DataRequired()])
    est_time = DecimalField('Est. time (in hours):', validators=[DataRequired()])
    price_ph = DecimalField('Price per hour:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddJobForm(FlaskForm):
    customer = SelectField('Customer:')
    task = SelectField('Task:')
    start_date = DateField('Start Date:', format='%d/%m/%Y', validators=[DataRequired()],default=date.today())
    # finish_date = DateField('Finish Date:', format='%d-%m-%Y', default=date.today)
    # complete = SelectField('Job Complete', default=False)
    complete = StringField('Complete')
    total_price = DecimalField('Total Price:')#, validators=[DataRequired()])#######
    submit = SubmitField('Submit')

class AddMaterialForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    desc = StringField('Description:', validators=[DataRequired()])
    supplier = StringField('Supplier:', validators=[DataRequired()])
    price = DecimalField('Price per:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMatUsedForm(FlaskForm):
    material_id = SelectField('Material:')
    quantity = IntegerField('Quantity:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditMaterialUsedForm(FlaskForm):
    quantity = IntegerField('Quantity:', validators=[DataRequired()])
    submit = SubmitField('Submit')