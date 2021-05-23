from sqlalchemy.orm import backref
from application import db
from datetime import date

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.task_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today())
    # finish_date = db.Column(db.Date, nullable=True)
    complete = db.Column(db.Boolean, nullable=False)
    materials_used = db.relationship('MaterialsUsed', backref='job')
    total_price = db.Column(db.Float(10,2), nullable=False, default=0.00)     

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    home_num = db.Column(db.String(15), nullable=False)
    mobile_num = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    town_city = db.Column(db.String(100), nullable=False)
    county = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    job = db.relationship('Jobs', backref='jobs')

class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    est_time = db.Column(db.Float(10,2), nullable=False)
    price_ph = db.Column(db.Float(10,2), nullable=False, default=0.00)
    job = db.relationship('Jobs', backref='jobs')
           
class Materials(db.Model):
    material_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    supplier = db.Column(db.String(100), nullable=False)        # could maybe add supplier table
    price = db.Column(db.Float(10,2), nullable=False, default=0.00)
    materials_used = db.relationship('MaterialsUsed', backref='material')

class MaterialsUsed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.material_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)  