from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
import sys

#redirect to login page
def GotoLoginPage():
    try:
        elem = driver.find_element_by_class_name('login')
        elem.click()
        return True   
    except NoSuchElementException:
        return False

#generate random data for register purpose
def generateRandomData():
    fake = Faker()
    d = dict()
    name = fake.name()
    names = name.split(" ")
    d['firstname'] = names[0]
    d['lastname'] =  names[1]
    d['email'] = fake.email()
    d['address'] = fake.street_address()
    d['city'] = fake.city()
    d['state'] = fake.state()
    d['postcode'] = fake.postcode()
    d['mobile'] = fake.random_number(digits=10, fix_len=False)
    return d

#function for register/sign up
def RegisterAcc(data):
    d = data
    elem2 = driver.find_element_by_id("email_create")
    elem2.send_keys("lucky_lyphee@yahoo.com")
    elem3 = driver.find_element_by_id("SubmitCreate")
    elem3.click()
    driver.implicitly_wait(15)
    elem4 = driver.find_element_by_id("customer_firstname")
    elem4.send_keys(d.get("firstname"))
    elem5 = driver.find_element_by_id("customer_lastname")
    elem5.send_keys(d.get("lastname"))
    elem6 = driver.find_element_by_id("passwd")
    elem6.send_keys("12345abc")
    elem7 = driver.find_element_by_id("firstname")
    elem7.send_keys(d.get("firstname"))
    elem8 = driver.find_element_by_id("lastname")
    elem8.send_keys(d.get("lastname"))
    elem9 = driver.find_element_by_id("address1")
    elem9.send_keys(d.get("address"))
    elem10 = driver.find_element_by_id("city")
    elem10.send_keys(d.get("city"))
    select = Select(driver.find_element_by_id('id_state'))
    select.select_by_visible_text(d.get("state"))
    elem11 = driver.find_element_by_id("postcode")
    elem11.send_keys(d.get("postcode"))
    elem12 = driver.find_element_by_id("phone_mobile")
    elem12.send_keys(d.get("mobile"))
    elem13 = driver.find_element_by_id("submitAccount")
    elem13.click()
    print "SIGN UP : SUCCESS"

#to input email and password in log in page
def InsertEmailPassword(email,passwd):
    elem14 = driver.find_element_by_id("email")
    elem14.clear()
    elem14.send_keys(email)
    elem15 = driver.find_element_by_id("passwd")
    elem15.clear()
    elem15.send_keys(passwd)
    elem16 = driver.find_element_by_id("SubmitLogin")
    elem16.click()

#check log in submission based on test case
def ValidationLogin(testcase, message):
    try:
        elem17 = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li')
        if message in elem17.text:
            print "LOGIN/" + testcase + " : PASSED"
        else:
            print "LOGIN/" + testcase + " : FAILED"
    except NoSuchElementException:
        print "LOGIN/" + testcase + " : FAILED"

#redirect to forgot password page
def GotoForgotPasswordPage():
    try:
        elem18 = driver.find_element_by_xpath('//*[@id="login_form"]/div/p[1]/a')
        elem18.click()
        return True   
    except NoSuchElementException:
        return False

#forgot password email validation 
def ForgotPassword(email, testcase, message):
    elem19 = driver.find_element_by_id("email")
    elem19.send_keys(email)
    elem20 = driver.find_element_by_xpath('//*[@id="form_forgotpassword"]/fieldset/p/button')
    elem20.click()
    driver.implicitly_wait(10)
    try:
        if(testcase == "12"):
            elem21 = driver.find_element_by_class_name('alert-success')
        else:
            elem21 = driver.find_element_by_class_name('alert-danger')
        if message in elem21.text:
            print "LOGIN/" + testcase + " : PASSED"
        else:
            print "LOGIN/" + testcase + " : FAILED"
    except NoSuchElementException:
        print "LOGIN/" + testcase + " : FAILED"
    elem22 = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/a')
    elem22.click()
    GotoForgotPasswordPage()

#log out function
def Logout():
    try:
        elem = driver.find_element_by_class_name('logout')
        elem.click()
        print "LOGIN/03 : PASSED"
    except NoSuchElementException:
        print "LOGIN/03 : FAILED"

#to execute all of login test cases
def Login():
    #Test Case LOGIN/01
    if(GotoLoginPage() == True):
        print "LOGIN/01 : PASSED"
    else:
        print "LOGIN/01 : FAILED"
    
    #Test Case LOGIN/02
    InsertEmailPassword("babyshark@dudu.com", "12345abc")
    try:
        elem17 = driver.find_element_by_class_name("info-account")
        print "LOGIN/02 : PASSED"
        #Test Case LOGIN/03
        Logout()
    except NoSuchElementException:
        print "LOGIN/02 : FAILED"
    GotoLoginPage()
    
    #Test Case LOGIN/04
    InsertEmailPassword("babyshark@dudu.com", "1234512345")
    ValidationLogin("04", "Authentication failed")
    
    #Test Case LOGIN/05
    InsertEmailPassword("babyshark@dudu.com", "1234")
    ValidationLogin("05", "Invalid password")
    
    #Test Case LOGIN/06
    InsertEmailPassword("babyshark@dudu", "12345abc")
    ValidationLogin("06", "Invalid email address")
    
    #Test Case LOGIN/07
    InsertEmailPassword("babyshark@dudu", "12345abcd")
    ValidationLogin("07", "Invalid email address")
    
    #Test Case LOGIN/08
    InsertEmailPassword("babysharkz@dudu.com", "12345abcd")
    ValidationLogin("08", "Authentication failed")
    
    #Test Case LOGIN/09
    elem14 = driver.find_element_by_id("email")
    elem14.clear()
    elem14.send_keys("babyshark@dudu.com")
    elem15 = driver.find_element_by_id("passwd")
    elem15.clear()
    elem16 = driver.find_element_by_id("SubmitLogin")
    elem16.click()
    ValidationLogin("09", "Password is required")
    
    #Test Case LOGIN/10
    elem14 = driver.find_element_by_id("email")
    elem14.clear()
    elem15 = driver.find_element_by_id("passwd")
    elem15.clear()
    elem15.send_keys("12345abc")
    elem16 = driver.find_element_by_id("SubmitLogin")
    elem16.click()
    ValidationLogin("10", "An email address required")
    
    #Test Case LOGIN/11
    if(GotoForgotPasswordPage() == True):
        print "LOGIN/11 : PASSED"
    else:
        print "LOGIN/11 : FAILED"
    
    #Test Case LOGIN/12    
    ForgotPassword("babyshark@dudu.com", "12", "confirmation email has been sent to your address")

    #Test Case LOGIN/14
    ForgotPassword("babyshark@dudu", "14", "Invalid email address")

    #Test Case LOGIN/15
    ForgotPassword("babysharkz@dudu.com", "15", "There is no account registered for this email address")


#input : python test.py register or python test.py login
command = sys.argv[1]
d = generateRandomData()
if (command.lower() == "register"):
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com")
    GotoLoginPage()
    RegisterAcc(d)
    driver.close()
elif (command.lower() == "login"):
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com")
    GotoLoginPage()
    Login()
    driver.close()
else:
    print "command not exist"


