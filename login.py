from selenium import webdriver
import os
import subprocess, platform


def site_login():
	driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect")
	driver.find_element_by_name("userId").send_keys("username")
	driver.find_element_by_name("password").send_keys("password")
	driver.find_element_by_name("Submit22").click()

def check_ping(sHost='www.google.com'):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception:
        return False

    return True


if __name__ == '__main__':
    print('Checking if Net Connection is working.... \n')

    if check_ping() ==False:
        driver = webdriver.Chrome('C:/Users/Saurav/Desktop/LoginModule/chromedriver.exe')
        site_login()
        if check_ping():
            print('Connection Initiated....')
            driver.quit()
        #input()            #Debugging purpose only
    else:
        print('Already connected...exiting....')
        #input()            #Debugging purpose only
