from unittest.runner import TextTestResult
from flask import url_for
from flask.globals import session
from flask.wrappers import Response
from flask_testing import TestCase
from sqlalchemy.ext.declarative.api import declarative_base
from application import db,app
from application.models import Customers,Tasks,Materials,MaterialsUsed,Jobs
from datetime import datetime

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY='asoijgpw89eu5t-0sd',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()

        new_customer=Customers(
            first_name='Jack',
            last_name='Parry',
            email='email@email.com',
            home_num='01777 777777',
            mobile_num='07777 777777',
            address='123 street',
            town_city='town',
            county='county',
            postcode='LL191AA'
        )
        new_task=Tasks(
            name='Boiler Change',
            desc='Change old boiler for new one',
            est_time=8,
            price_ph=60
        )
        new_job=Jobs(
            customer_id=1,
            task_id=1,
            start_date=datetime.strptime('12-04-2021', '%d-%m-%Y'),
            complete=False,
            total_price=new_task.est_time*new_task.price_ph
        )
        new_material=Materials(
            name='Gas Worcester Boiler',
            desc='Brand new gas Worcester boiler for heating hour home',
            supplier='Plumbs Center',
            price=1200
        )

        new_matsused=MaterialsUsed(
            job_id=1,
            material_id=1,
            quantity=1
        )
        db.session.add(new_customer)
        db.session.add(new_task)
        db.session.add(new_job)
        db.session.add(new_material)
        db.session.add(new_matsused)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response=self.client.get(url_for('Index'))
        self.assertEqual(response.status_code, 200)

    def test_addcustomer_get(self):
        response=self.client.get(url_for('AddCustomer'))
        self.assertEqual(response.status_code, 200)
    
    def test_addtask_get(self):
        response=self.client.get(url_for('AddTask'))
        self.assertEqual(response.status_code, 200)
    
    def test_addjob_get(self):
        response=self.client.get(url_for('AddJob'))
        self.assertEqual(response.status_code, 200)
    
    def test_addmaterial_get(self):
        response=self.client.get(url_for('AddMaterial'))
        self.assertEqual(response.status_code, 200)
    
    def test_addmaterialused_get(self):
        response=self.client.get(url_for('AddMaterialsUsed', job_id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_editcustomer_get(self):
        response=self.client.get(url_for('EditCustomer',id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_edittask_get(self):
        response=self.client.get(url_for('EditTask',id=1))
        self.assertEqual(response.status_code, 200)

    def test_editjob_get(self):
        response=self.client.get(url_for('EditJob',id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_editmaterial_get(self):
        response=self.client.get(url_for('EditMaterial',id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_editmatused_get(self):
        response=self.client.get(url_for('EditMatsUsed',id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_showcustomers_get(self):
        response=self.client.get(url_for('ShowCustomers'))
        self.assertEqual(response.status_code, 200)
    
    def test_showtasks_get(self):
        response=self.client.get(url_for('ShowTasks'))
        self.assertEqual(response.status_code, 200)

    def test_showmaterials_get(self):
        response=self.client.get(url_for('ShowMats'))
        self.assertEqual(response.status_code, 200)

    def test_showmatsused_get(self):
        response=self.client.get(url_for('ShowMatsUsed', job_id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_viewcustomer_get(self):
        response=self.client.get(url_for('ViewCustomer', id=1))
        self.assertEqual(response.status_code, 200)

    def test_viewtask_get(self):
        response=self.client.get(url_for('ViewTask', id=1))
        self.assertEqual(response.status_code, 200)

    def test_viewmaterial_get(self):
        response=self.client.get(url_for('ViewMaterial', id=1))
        self.assertEqual(response.status_code, 200)


class TestAdd(TestBase):
    def test_addcustomer_post(self):
        response = self.client.post(
            url_for('AddCustomer'),
            data = dict(
                first_name='Clark',
                last_name='Kent',
                email='sman@email.com',
                home_num='01222 222222',
                mobile_num='07666 666666',
                address='1 street',
                town_city='Smallville',
                county='Krypton',
                postcode='SS1 1SS'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Clark', response.data)

    def test_addtask_post(self):
        response = self.client.post(
            url_for('AddTask'),
            data = dict(
                name='Change oil tank',
                desc='Change out old or broken oil tank for a brand new one',
                est_time=4,
                price_ph=50
            ),
            follow_redirects=True
        )
        self.assertIn(b'Change oil tank', response.data)

    def test_addjob_post(self):
        response = self.client.post(
            url_for('AddJob'),
            data = dict(
                customer_id=2,
                task_id=1,
                start_date=datetime.strptime('20-05-2021', '%d-%m-%Y'),
                complete=False
            ),
            follow_redirects=True
        )
        self.assertIn(b'1', response.data)
    
    def test_addmat_post(self):
        response = self.client.post(
            url_for('AddMaterial'),
            data = dict(
                name='New Oil Tank',
                desc='A brand new oil tank for storing oil',
                supplier='Plumb Center',
                price=500
            ),
            follow_redirects=True
        )
        self.assertIn(b'New Oil Tank', response.data)

    def test_addmatused_post(self):
        response = self.client.post(
            url_for('AddMaterialsUsed',job_id=1),
            data = dict(
                job_id=1,
                material_id=2,
                quantity=1
            ),
            follow_redirects=True
        )
        self.assertIn(b'1', response.data)

class TestUpdate(TestBase):
    def test_updatecustomer(self):
        response = self.client.post(
            url_for('EditCustomer', id=1),
            data = dict(
                first_name='Jack',
                last_name='Larry',
                email='email@gmail.com',
                home_num='01777 777777',
                mobile_num='07777 777777',
                address='123 street',
                town_city='town',
                county='county',
                postcode='LL191AA'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Larry', response.data)
    
    def test_updatetask(self):
        response = self.client.post(
            url_for('EditTask', id=1),
            data = dict(
               name='Oil Worcester Boiler',
               desc='Change old boiler for new one',
               est_time='7',
               price_ph=60
            ),
            follow_redirects=True
        )
        self.assertIn(b'Oil Worcester Boiler', response.data)

    def test_updatejob(self):
        response = self.client.post(
            url_for('EditJob', id=1),
            data = dict(
               customer_id=1,
               task_id=1,
               start_price=datetime.strptime('20-05-2021', '%d-%m-%Y'),
               complete=True
            ),
            follow_redirects=True
        )
        self.assertIn(b'True', response.data)

    def test_updatemat(self):
        response = self.client.post(
            url_for('EditMaterial', id=1),
            data = dict(
                name='Oil Boiler Change',
                desc='Brand new oil Worcester boiler for heating hour home',
                supplier='Plumb Center',
                price=1200
            ),
            follow_redirects=True
        )
        self.assertIn(b'Oil Boiler Change', response.data)
    
    def test_updatematused(self):
        response = self.client.post(
            url_for('EditMatsUsed', id=1),
            data = dict(
                job_id=1,
                material_id=1,
                quantity=2
            ),
            follow_redirects=True
        )
        self.assertIn(b'2', response.data)


