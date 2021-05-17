from application.forms import AddCustomerForm, AddJobForm, AddTaskForm
from logging import error
from flask import render_template, request, redirect, url_for
from application import app,db
from application.models import Customers, Tasks, Jobs, Materials, MaterialsUsed

@app.route('/')
def Index():
    all_jobs = Jobs.query.all()
    all_customers = Customers.query.all()
    all_tasks = Tasks.query.all()
    return render_template('index.html', jobs=all_jobs, customers=all_customers, tasks=all_tasks)

@app.route('/add customer', methods=['GET', 'POST'])
def AddCustomer():
    form = AddCustomerForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        home_num = form.home_num.data
        mobile_num = form.mobile_num.data
        address = form.address.data
        town_city = form.town_city.data
        county = form.county.data
        postcode = form.postcode.data

        if form.validate_on_submit():
            new_customer = Customers(
                first_name=first_name,
                last_name=last_name,
                email=email,
                home_num=home_num,
                mobile_num=mobile_num,
                address=address,
                town_city=town_city,
                county=county,
                postcode=postcode)
            db.session.add(new_customer)
            db.session.commit()
            return redirect(url_for('Index'))
        
    return render_template('add_customer.html', form = form)


@app.route('/add task', methods=['GET', 'POST'])
def AddTask():
    form = AddTaskForm()
    if request.method == 'POST':
        name = form.name.data
        desc = form.desc.data
        est_time = form.est_time.data
        price_ph = form.price_ph.data

        if form.validate_on_submit():
            new_task = Tasks(
                name=name,
                desc=desc,
                est_time=est_time,
                price_ph = price_ph
            )
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('Index'))

    return render_template('add_task.html', form = form)


@app.route('/add job',  methods=['GET', 'POST'])
def AddJob():
    form = AddJobForm()
    # all_customers=Customers.query.all()
    # all_tasks=Tasks.query.all()

    if request.method == 'POST':
        customer_id = form.customer.data
        customer_id = customer_id.split()
        customer_id = customer_id[0]
        task_id = form.task.data
        task_id = task_id.split()
        task_id = task_id[0]

        if form.validate_on_submit():
            new_job = Jobs(
                customer_id=customer_id,
                task_id=task_id
            )
            db.session.add(new_job)
            print(new_job)
            db.session.commit()
            return redirect(url_for('Index'))
            
    return render_template('add_job.html', form = form)#, all_customers=all_customers, all_tasks=all_tasks)