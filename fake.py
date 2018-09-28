from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker
import sys


def RegisterAcc():
    elem2 = driver.find_element_by_id("email_create")
    elem2.send_keys("babyshark@dudu.com")
    elem3 = driver.find_element_by_id("SubmitCreate")
    elem3.click()
    driver.implicitly_wait(15)
    elem4 = driver.find_element_by_id("customer_firstname")
    elem4.send_keys("Harrison")
    elem5 = driver.find_element_by_id("customer_lastname")
    elem5.send_keys("Ford")
    elem6 = driver.find_element_by_id("passwd")
    elem6.send_keys("12345abc")
    elem7 = driver.find_element_by_id("firstname")
    elem7.send_keys("Harrison")
    elem8 = driver.find_element_by_id("lastname")
    elem8.send_keys("Ford")
    elem9 = driver.find_element_by_id("address1")
    elem9.send_keys("Happiness Street across the road No. 1")
    elem10 = driver.find_element_by_id("city")
    elem10.send_keys("Jakarta")
    select = Select(driver.find_element_by_id('id_state'))
    select.select_by_visible_text('California')
    elem11 = driver.find_element_by_id("postcode")
    elem11.send_keys("12345")
    elem12 = driver.find_element_by_id("phone_mobile")
    elem12.send_keys("123456789")
    elem13 = driver.find_element_by_id("submitAccount")
    elem13.click()

def generateName():
    fake = Faker()
    d = dict()
    name = fake.name()
    names = name.split(" ")
    d['firstname'] = names[0]
    d['lastname'] =  names[1]
    d['email'] = fake.email()
    d['password'] = "12345abc"
    d['address'] = fake.street_address()
    d['city'] = fake.city()
    d['state'] = fake.state()
    d['postcode'] = fake.postcode()
    d['mobile'] = fake.random_number(digits=10, fix_len=False)
    
    
    return d

def generateEmail():
    fake = Faker()
    email = fake.email()
    return email

d = generateName()
print d
print d.get("mobile")