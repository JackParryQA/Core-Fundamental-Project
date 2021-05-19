from sqlalchemy.orm import query
from wtforms.fields.core import DateField, IntegerField
from application.models import Customers, Materials, Tasks
from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, SubmitField, FloatField, TimeField, SelectField
from wtforms.validators import DataRequired, AnyOf, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class AddCustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    home_num = StringField('Home Number', validators=[DataRequired()])
    mobile_num = StringField('Mobile Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    town_city = StringField('Town/City', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Add Customer')

class AddTaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    est_time = FloatField('Est. time (in hours)', validators=[DataRequired()])
    price_ph = FloatField('Price per hour', validators=[DataRequired()])
    submit = SubmitField('Add Task')

class AddJobForm(FlaskForm):
    customer = SelectField('Customer')
    task = SelectField('Task')
    start_date = DateField('Start Date', validators=[DataRequired()])
    finish_date = DateField('Finish Date')
    total_price = FloatField('Total Price', validators=[DataRequired()])#######
    submit = SubmitField('Add Job')

class AddMaterialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    supplier = StringField('Supplier', validators=[DataRequired()])
    price = FloatField('Price per', validators=[DataRequired()])
    submit = SubmitField('Add Material')

class AddMatUsedForm(FlaskForm):
    job_id = SelectField('Job')
    material_id = SelectField('Material')
    quantity = IntegerField('Quantity')