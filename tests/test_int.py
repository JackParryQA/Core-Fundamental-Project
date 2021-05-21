from flask.helpers import url_for
from flask_testing import LiveServerTestCase
from application import app,db
# from application.models import Customers,Tasks,Materials,MaterialsUsed,Jobs
# from datetime import datetime
from selenium import webdriver
from urllib.request import urlopen


class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///int-test.db",
                SECRET_KEY='dsfgsegsdgh53rsn',
                DEBUG=True,
                TESTING=True)
        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() # create schema before we try to get the page

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    
    def test_server_is_up_and_running(self):
        response = urlopen(url_for('{self.TEST_PORT}'))
        self.assertEqual(response.code, 200)

class TestInt(TestBase):
    # add customer for later

    def test_addcustomer_int(self):
        self.driver.get(url_for('AddTask'))
        
        name_input = self.driver.find_element_by_xpath('//*[@id="name"]')
        name_input.send_keys('Fit Radiator')
        # desc_input = self.driver.find_element_by_xpath('//*[@id="desc"]')
        # desc_input.send_keys('Fit brand new radiator to wall')
        # est_time_input = self.driver.find_element_by_xpath('//*[@id="est_time"]')
        # est_time_input.send_keys('2')
        # price_input = self.driver.find_element_by_xpath('//*[@id="price_ph"]')
        # price_input.send_keys('20')
        
        price_input = self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        assert self.driver.current_url == url_for('ShowTasks')
    
    #  def test_create(self):
        # self.driver.get(f'http://localhost:5000/create') # go to /create route

        # input_box = self.driver.find_element_by_xpath('//*[@id="name"]')
        # input_box.send_keys('Hello World')

        # self.driver.find_element_by_xpath('//*[@id="submit"]').click() # submit field

        # assert self.driver.current_url == 'http://localhost:5000/index'