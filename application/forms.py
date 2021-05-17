from sqlalchemy.orm import query
from application.models import Customers, Tasks
from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, SubmitField, FloatField, TimeField, SelectField
from wtforms.validators import DataRequired, AnyOf, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class AddCustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
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
    all_customers = Customers.query.all()
    all_tasks = Tasks.query.all()

    customers_list = list()
    for i in all_customers:
        customers_list.append(f"{i.customer_id} {i.first_name} {i.last_name}")

    tasks_list = list()
    for i in all_tasks:
        tasks_list.append(f"{i.task_id} {i.name}")

    customer = SelectField('Customer', choices=customers_list)#, validators=[AnyOf(all_customers, message='Please select a customer')])
    task = SelectField('Task', choices=tasks_list)#, validators=[AnyOf(all_tasks, message='Please select a task')])
    submit = SubmitField('Add Job')
    
    
    # customer = SelectField('Customer')
    # task = SelectField('Task')

    # def set_choices(self):
    #         self.customer.choices=query(Customers).all()

    # def __init__(self, *args, **kwargs):
    #     super(AddJobForm,self).__init__(*args, **kwargs)
    #     self.customer.choices=[(c.customer_id, c.first_name) for c in Customers.query.all()] and [(c.customer_id, c.last_name) for c in Customers.query.all()]
        # self.customer.choices=set_choices()

    

