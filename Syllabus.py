from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
'''
This program will get all your syllabus courses of the current year.

'''


#Run the program and put your username and password.

# Defines the user name and password and sets basic things for the browser
class MySyllabus:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        pre = {'download_dir': 'C:/Users/Omer/Downloads'} # define the Download dir.
        options.add_experimental_option("prefs",pre)
        options.binary_location = 'C:/Users/Omer/AppData/Local/Google/Chrome SxS/Application/chrome.exe'
        self.bot = webdriver.Chrome(chrome_options=options)

# Connects and returns the unique number to that login
    def login(self):
        bot = self.bot
        time.sleep(3)
        bot.get('https://meyda.ariel.ac.il/michlol3/StudentPortalWap/Pt_login.aspx')
        username = bot.find_element_by_name('ctl00_idMasterContentPlaceHolder_IdentityNumber_text')
        password = bot.find_element_by_name('ctl00_idMasterContentPlaceHolder_SecretCode_text')
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        return bot.current_url.split('?')[-1]

# Chains the unique login number received in the login function and enters the page of all courses
    def MyCoursesPage(self,url):
        bot = self.bot
        bot.get('https://meyda.ariel.ac.il/michlol3/StudentPortalWap/PT_MYCOURSES.ASPX?guid='+url+'&treecode=06.01')
        time.sleep(3)
        allyears = bot.find_element_by_id('ctl00_idMasterContentPlaceHolder_ddlKrsSms_Input')
        allyears.clear()
        allyears.send_keys('כל הסמסטרים')
        allyears.send_keys(Keys.ENTER)

# Collects all objects that hold syllabus and downloads all
    def getData(self):
        time.sleep(2)
        bot = self.bot
        coursesPointer = bot.find_elements_by_id('ctl00_idMasterContentPlaceHolder_idMyCourses_GridData')
        coursesPointer = bot.find_elements_by_id('ctl00_idMasterContentPlaceHolder_idMyCourses_ctl00')
        final_List_Of_Syllabuses = [];
        for i in bot.find_elements_by_tag_name('input'):
            if (i.get_attribute('title') == 'סילבוס'):
                final_List_Of_Syllabuses.append(i.get_attribute('id'))

        try:
            for i in final_List_Of_Syllabuses:
                time.sleep(2)
                bot.find_element_by_id(i).click()

        except Exception as ex:
            print(ex)
            bot.close()

        finally:
            time.sleep(3)
            bot.close()



auto =  MySyllabus('', '')
idLogin = auto.login()
auto.MyCoursesPage(idLogin)
auto.getData()