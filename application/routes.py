from application.forms import AddCustomerForm, AddJobForm, AddMaterialForm, AddTaskForm
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
            print('hello')
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

# def SelectCustomers():
#     return Customers.query

@app.route('/add job',  methods=['GET', 'POST'])
def AddJob():
    all_customers=Customers.query.all()
    customer_ids = list()
    for i in all_customers:
        customer_ids.append(i.customer_id)

    all_tasks=Tasks.query.all()
    task_ids = list()
    for i in all_tasks:
        task_ids.append(i.task_id)

    form = AddJobForm()
    form.customer.choices=customer_ids
    form.task.choices=task_ids
    # form.customer.query_factory=SelectCustomers

    if request.method == 'POST':
        customer_id = form.customer.data
        task_id = form.task.data
        start_date = form.start_date.data
        finish_date = form.finish_date.data
        total_price = form.total_price.data##############
        
        if form.validate_on_submit():
            new_job = Jobs(
                customer_id=customer_id,
                task_id=task_id,
                start_date=start_date,
                finish_date=finish_date,
                total_price=total_price
            )
            print(new_job)
            
            db.session.add(new_job)
            db.session.commit()
            return redirect(url_for('Index'))
    return render_template('add_job.html', form = form)

@app.route('/add material', methods=['GET','POST'])
def AddMaterial():
    form = AddMaterialForm()
    if request == 'POST':
        name = form.name.data
        desc = form.desc.data
        supplier = form.supplier.data
        price = form.price.data

        if form.validate_on_submit():
            new_mat = Materials(
                name = name,
                desc = desc,
                supplier = supplier,
                price = price
            )
            db.session.add(new_mat)
            db.session.commit()
            return redirect(url_for('AddTask'))

    return render_template('add_material.html', form = form)
