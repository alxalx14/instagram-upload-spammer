from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
import autoit
import random

class main:

	

    def __init__(self, username, password):
        
        self.chromeOptions = Options()
        self.stealthUA = "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"
        self.chromeOptions.add_argument(f"user-agent={self.stealthUA}")
        self.driver = webdriver.Chrome(chrome_options=self.chromeOptions)
        url = "instagram.com"
        self.driver.get("https://" + url + "/")
        sleep(2)
        self.loginBtn = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button")
        self.loginBtn.click()
        sleep(4)
        self.inputUser = self.driver.find_element_by_xpath("//html/body/div[1]/section/main/article/div/div/div/form/div[4]/div/label/input")
        self.inputPass = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[5]/div/label/input")
        self.inputUser.send_keys(username)
        sleep(2)
        self.inputPass.send_keys(password)
        self.loginAction = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]")
        sleep(1)
        self.loginAction.click()
        input("Press Enter When on main Page !")
        sleep(2)
        i = 0
        self.picsToChoose = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png"]
        for i in range(10000):
        	

            try:
                self.cancelHS = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
                self.cancelHS.click()
            except:
                pass


            self.chosenYoda = random.choice(self.picsToChoose)
            self.imgPath = f"pictures\\{self.chosenYoda}"
            sleep(2)
            self.upload1 = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]")
            self.upload1.click()
            autoit.win_active("Open") 
            sleep(1)
            autoit.control_send("Open","Edit1",self.imgPath) 
            sleep(2)
            autoit.control_send("Open","Edit1","{ENTER}")
            sleep(1)
            self.upload2 = self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
            self.upload2.click()
            sleep(1)
            self.upload3 = self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea")
            self.upload3.send_keys("""Baby Yoda FTW       #memes #like #funny #yoda #starwars""")
            sleep(2)
            self.uploadFinal = self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
            self.uploadFinal.click()
            sleep(6)
            try:
            	self.ntN = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
            	self.ntN.click()
            except:
            	pass
            i+=1
            print(f"Uploaded PIC No. {i}")
            if(i == 60):
            	i = 0
            	sleep(10)
            else:
            	sleep(1)


#url = input("Whats the Website?\n>")
pwFile = open("loginData.txt" ,'r')
loginData = pwFile.readlines()
rawName = loginData[0]
username = rawName.replace("\n", "")
rawPass = loginData[1]
password = rawPass.replace("\n", "")
#print(f"Username: {username}\nPassword: {password}")
      
main(username, password)
