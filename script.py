from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os 

now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
 # %A is to get the name of the Day!
justtime = now.strftime("%H:%M")
print (current_time)

#  Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

# Conditions to check time and append if necessary
'''while justtime !=  "10:27" or justtime != "13:50" or justtime != "15:20" or  justtime != "16:50":
    time.sleep(20)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    justtime = now.strftime("%H:%M")
    print(justtime)
    if justtime == "09:50" or justtime == "13:50" or justtime == "15:20" or  justtime == "16:50":
        print("Class is going to start in 10 Minutes.")
        break'''
    
# directing to the link to be visited; The program first logs into gmail for all around access of google services.
def gmail_login():
        #login to stackoverflow account
    driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
    time.sleep(4)
        #login with google account
    driver.find_element_by_xpath('''//*[@id="openid-buttons"]/button[1]''').click()
    time.sleep(5)
        #email
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("chiragchauhan12323@gmail.com")
    time.sleep(5)
        #next button:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(2)
        #password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys("chiragchauhan12323")
    time.sleep(5)
        #next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
        # #opening Meet:
    driver.get(sub)
    driver.refresh()
    time.sleep(10)
    ''' # Turning off video 
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    time.sleep(5)
        # turning off audio
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
    time.sleep(180)'''
        # Join class
        
    driver.find_element_by_xpath('''//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span''').click()

# Conditions which checks the time and goes to the classlink if Classes are happening at that time.

# Class1  Subject - ACA
if current_time == "20:23 / Tuesday" or current_time == "10:10 / Monday" or current_time == "12:00 / Tuesday" or current_time == "12:10 / Tuesday" or current_time == "11:00 / Wednesday" or current_time == "11:10 / Wednesday" or current_time == "01:40 / Friday" or current_time == "01:50 / Friday":
    sub = "https://meet.google.com/nmf-jimc-kis"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver.exe') 
    gmail_login()
    

# Class2 Subject - NN
elif current_time == "20:25 / Tuesday" or current_time == "10:15 / Monday" or current_time == "01:40 / Wednesday" or current_time == "01:50 / Wednesday" or current_time == "12:00 / Thursday" or current_time == "12:10 / Thursday" or current_time == "10:00 / Friday" or current_time == "10:10 / Friday":
    sub = "https://meet.google.com/efw-ygig-sph"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# Class3 Subject - SPM
elif current_time == "12:00 / Monday" or current_time == "12:10 / Monday" or current_time == "10:00 / Tuesday" or current_time == "10:10 / Tuesday" or current_time == "11:00 / Thursday" or current_time == "11:10 / Thursday" or current_time == "02:40 / Friday" or current_time == "02:50 / Friday":
    sub = "###Google meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Class4 Subject - CD
elif current_time == "01:40 / Monday" or current_time == "01:50 / Monday" or current_time == "11:00 / Tuesday" or current_time == "11:10 / Tuesday" or current_time == "10:00 / Wednesday" or current_time == "10:10 / Wednesday" or current_time == "11:00 / Friday" or current_time == "11:10 / Friday":
    sub = "###Google meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Class5 Subject - AJ
elif current_time == "02:40 / Monday" or current_time == "02:50 / Monday" or current_time == "01:40 / Tuesday" or current_time == "01:50 / Tuesday" or current_time == "12:00 / Wednesday" or current_time == "12:10 / Wednesday" or current_time == "01:40 / Thursday" or current_time == "01:50 / Thursday" :
    sub = "###Google meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Class6 Subject - DOS
elif current_time == "02:40 / Tuesday" or current_time == "02:50 / Tuesday" or current_time == "02:40 / Wednesday" or current_time == "02:50 / Wednesday" or current_time == "10:00 / Thursday" or current_time == "10:10 / Thursday" or current_time == "12:00 / Friday" or current_time == "12:10 / Friday":
    sub = "###Google meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

else:
    print("No classes right now")
