import re
from application.forms import AddCustomerForm, AddJobForm, AddMatUsedForm, AddMaterialForm, AddTaskForm, EditMaterialUsedForm
from flask import render_template, request, redirect, url_for
from application import app,db
from application.models import Customers, Tasks, Jobs, Materials, MaterialsUsed

@app.route('/')
def Index():
    all_jobs = Jobs.query.all()
    all_customers = Customers.query.all()
    all_tasks = Tasks.query.all()
    all_matsused = MaterialsUsed.query.all()
    return render_template('index.html', jobs=all_jobs, customers=all_customers, tasks=all_tasks, mats=all_matsused)

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
            return redirect(url_for('ShowCustomers'))
        
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
            return redirect(url_for('ShowTasks'))

    return render_template('add_task.html', form = form)

@app.route('/add job',  methods=['GET', 'POST'])
def AddJob():
    all_customers=Customers.query.all()
    customers = list()
    for i in all_customers:
        customers.append(tuple((i.customer_id, f'{i.first_name} {i.last_name}')))

    all_tasks=Tasks.query.all()
    task_ids = list()
    for i in all_tasks:
        task_ids.append(tuple((i.task_id,i.name)))

    form = AddJobForm()
    form.customer.choices=customers
    form.task.choices=task_ids
    # form.complete.choices=(((False,False)),((True,True)))
    if request.method == 'POST':
        customer_id = form.customer.data
        task_id = form.task.data
        start_date = form.start_date.data
        # complete = bool(form.complete.data)
        # temp=Tasks.query.get(task_id)
        # total_price = temp.est_time*temp.price_ph
        if form.validate_on_submit():
            new_job = Jobs(
                customer_id=customer_id,
                task_id=task_id,
                start_date=start_date,
                complete=False,
                total_price=0
            )
            db.session.add(new_job)
            db.session.commit()
            return redirect(url_for('UpdateJobPrice',type='add', id=new_job.job_id))
    return render_template('add_job.html', form = form)

@app.route('/add material', methods=['GET', 'POST'])
def AddMaterial():
    form = AddMaterialForm()
    if request.method == 'POST':
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
            return redirect(url_for('ShowMats'))

    return render_template('add_material.html', form = form)

@app.route('/materials used/<int:job_id>', methods=['GET', 'POST'])
def AddMaterialsUsed(job_id):
    form = AddMatUsedForm()
    all_mats=Materials.query.all()
    mat_ids=list()
    for i in all_mats:
        mat_ids.append(tuple((i.material_id, i.name)))
    form.material_id.choices=mat_ids
    if request.method == 'POST':
        material_id=form.material_id.data
        quantity=form.quantity.data
        if form.validate_on_submit():
            new_mat = MaterialsUsed(
                job_id=job_id,
                material_id=material_id,
                quantity=quantity
            )
            db.session.add(new_mat)
            db.session.commit()
            return redirect(url_for('UpdateJobPrice',type='add',id=job_id))
    return render_template('materials_used.html', form=form, job_id=job_id)


@app.route('/show materials used/<int:job_id>', methods=['GET', 'POST'])
def ShowMatsUsed(job_id):
    all_matsused = MaterialsUsed.query.filter_by(job_id=job_id).all()
    all_mats = Materials.query.all()
    return render_template('show_matsused.html', matsused=all_matsused, mats=all_mats, job_id=job_id)

@app.route('/customers')
def ShowCustomers():
    all_customers=Customers.query.all()
    return render_template('show_customers.html', customers=all_customers)

@app.route('/edit customer/<int:id>', methods=['GET', 'POST'])
def EditCustomer(id):
    form=AddCustomerForm()
    customer=Customers.query.get(id)
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
            customer.first_name=first_name
            customer.last_name=last_name
            customer.email=email
            customer.home_num=home_num
            customer.mobile_num=mobile_num
            customer.address=address
            customer.town_city=town_city
            customer.county=county
            customer.postcode=postcode
            db.session.commit()
            return redirect(url_for('ShowCustomers'))
    elif request.method=='GET':
        form.first_name.data = customer.first_name
        form.last_name.data = customer.last_name
        form.email.data = customer.email
        form.home_num.data = customer.home_num
        form.mobile_num.data = customer.mobile_num
        form.address.data = customer.address
        form.town_city.data = customer.town_city
        form.county.data = customer.county
        form.postcode.data = customer.postcode
    return render_template('edit_customer.html', form=form, id=id)

@app.route('/tasks')
def ShowTasks():
    all_tasks=Tasks.query.all()
    return render_template('show_tasks.html', tasks=all_tasks)

@app.route('/edit task/<int:id>', methods=['GET', 'POST'])
def EditTask(id):
    form=AddTaskForm()
    task=Tasks.query.get(id)
    if request.method=='POST':
        name=form.name.data
        desc=form.desc.data
        est_time=form.est_time.data
        price_ph=form.price_ph.data
        if form.validate_on_submit():
            task.name=name
            task.desc=desc
            task.est_time=est_time
            task.price_ph=price_ph
            db.session.commit()
            return redirect(url_for('ShowTasks'))
    elif request.method=='GET':
        form.name.data=task.name
        form.desc.data=task.desc
        form.est_time.data=task.est_time
        form.price_ph.data=task.price_ph
    return render_template('edit_task.html', form=form, id=id)

@app.route('/materials')
def ShowMats():
    all_mats=Materials.query.all()
    return render_template('show_mats.html', mats=all_mats)

@app.route('/edit material/<int:id>', methods=['GET', 'POST'])
def EditMaterial(id):
    form=AddMaterialForm()
    material=Materials.query.get(id)
    if request.method=='POST':
        name=form.name.data
        desc=form.desc.data
        supplier=form.supplier.data
        price=form.price.data
        if form.validate_on_submit():
            material.name=name
            material.desc=desc
            material.supplier=supplier
            material.price=price
            db.session.commit()
            return redirect(url_for('UpdateJobPrice',type='upd',id=id))
    elif request.method=='GET':
        form.name.data=material.name
        form.desc.data=material.desc
        form.supplier.data=material.supplier
        form.price.data=material.price
    return render_template('edit_mats.html', form=form, id=id)

@app.route('/edit job/<int:id>', methods=['GET', 'POST'])
def EditJob(id):
    all_customers=Customers.query.all()
    customers = list()
    for i in all_customers:
        customers.append(tuple((i.customer_id, f'{i.first_name} {i.last_name}')))

    all_tasks=Tasks.query.all()
    task_ids = list()
    for i in all_tasks:
        task_ids.append(tuple((i.task_id,i.name)))

    form = AddJobForm()
    form.customer.choices=customers
    form.task.choices=task_ids
    # form.complete.choices=((False,False),(True,True))
    job=Jobs.query.get(id)
    

    if request.method=='POST':
        customer=form.customer.data
        task=form.task.data
        start=form.start_date.data
        if form.validate_on_submit():
            job.customer=customer
            job.task=task
            job.start_date=start
            db.session.commit()
            return redirect(url_for('Index'))
    elif request.method=='GET':
        form.customer.data=job.customer_id
        form.task.data=job.task_id              #find how to display data in select field
        form.start_date.data=job.start_date
        # form.complete.data=job.complete
        # form.total_price=job.total_price
    return render_template('edit_job.html', form=form, id=id, price=job.total_price)

@app.route('/edit materials used/<int:id>', methods=['GET', 'POST'])
def EditMatsUsed(id):
    form=EditMaterialUsedForm()
    mats=MaterialsUsed.query.get(id)
    job=Jobs.query.get(id)
    mat=Materials.query.get(mats.material_id)
    if request.method=='POST':
        quantity=form.quantity.data
        price=quantity*mat.price
        if form.validate_on_submit():
            mats.quantity=quantity
            mats.price=price
            db.session.commit()
            return redirect(url_for('ShowMatsUsed',job_id=id))
    elif request.method=='GET':
        form.quantity.data=mats.quantity
    return render_template('edit_matsused.html', form=form,mat=mat,job=job,mats=mats)



@app.route('/delete/<tdb>/<int:id>')
def Delete(tdb,id):
    target=''
    if tdb=='Customers':
        target=Customers.query.get(id)
        jobs=Jobs.query.filter_by(customer_id=id)
        for i in jobs:
            db.session.delete(i)
        db.session.delete(target)
        db.session.commit()
        return redirect(url_for('ShowCustomers'))
    elif tdb=='Tasks':
        target=Tasks.query.get(id)
        tasks=Jobs.query.filter_by(task_id=id)
        for i in tasks:
            db.session.delete(i)
        db.session.delete(target)
        db.session.commit()
        return redirect(url_for('ShowTasks'))
    elif tdb=='Materials':
        target=Materials.query.get(id)
        mats_used=MaterialsUsed.query.filter_by(material_id=id)
        for i in mats_used:
            db.session.delete(i)
        db.session.delete(target)
        db.session.commit()
        return redirect(url_for('ShowMats'))
    elif tdb=='MaterialsUsed':
        target=MaterialsUsed.query.get(id)
        job_id=target.job_id
        db.session.delete(target)
        db.session.commit()
        return redirect(url_for('ShowMatsUsed',job_id=job_id))
    elif tdb=='Jobs':
        target=Jobs.query.get(id)
        mats_used=MaterialsUsed.query.filter_by(job_id=target.job_id)
        for i in mats_used:
            db.session.delete(i)
        db.session.delete(target)
        db.session.commit()
        return redirect(url_for('Index'))
    
@app.route('/update price/<type>/<int:id>')
def UpdateJobPrice(type,id):
    job=Jobs.query.get(id)
    all_mats=Materials.query.all()
    mats_used=MaterialsUsed.query.filter_by(job_id=id).all()
    # if len(Jobs.query.all()):
    task=Tasks.query.filter_by(task_id=job.task_id).first()
    total_price=0
    for i in mats_used:#MaterialsUsed table
        for j in all_mats:#Materials table
            if j.material_id==i.material_id:
                total_price+=i.quantity*j.price
    job.total_price=total_price+(task.est_time*task.price_ph)
    db.session.commit()
    if type=='del' :
        return redirect(url_for('ShowMatsUsed',job_id=id))
    elif type=='add':
        return redirect(url_for('Index'))
    elif type=='upd':
        return redirect(url_for('ShowMats'))


@app.route('/view customer/<int:id>')
def ViewCustomer(id):
    customer=Customers.query.get(id)
    return render_template('view_customer.html',customer=customer)

@app.route('/view task/<int:id>')
def ViewTask(id):
    task=Tasks.query.get(id)
    return render_template('view_task.html',task=task)

@app.route('/view material/<int:id>')
def ViewMaterial(id):
    mat=Materials.query.get(id)
    return render_template('view_material.html', mat=mat)

@app.route('/complete/<int:id>')
def CompleteJob(id):
    job=Jobs.query.get(id)
    job.complete=True
    db.session.commit()
    return redirect(url_for('Index'))

@app.route('/incomplete/<int:id>')
def InCompleteJob(id):
    job=Jobs.query.get(id)
    job.complete=False
    db.session.commit()
    return redirect(url_for('Index'))