# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException 
import random

class InstaPy():
    
    def __init__(self):
        self.chrome_options = Options()     
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)    
    ### ---> login
    ###Function is responsible for open browser and login with username and password.
    def login(self):
        self.login = "blazesienna" ### <--- Tu wprowadź login
        self.password = "FKllWXA4CQ3vrBX" ### <--- Tu wprowadź hasło
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        #---> click to accept cookies.    
        self.acceptbutton = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        time.sleep(2)
        self.acceptbutton.click()
        time.sleep(2)
        ##---> end    
        self.emailForm = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        time.sleep(1)
        self.passwordForm = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        time.sleep(1)
        self.loginButton = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        time.sleep(1)
        self.loginButton.click()
        time.sleep(15)


    ### ---> add_hashtags_and_search
    ### Function is responsible for open and run browser with random hashtag form hashtags[]
    def add_hashtags_and_search(self):   
        
        self.hashtags = ["love","instagood","photooftheday",
    "fashion",
    "beautiful",
    "happy",
    "cute",
    "tbt",
    "like4like",
    "followme",
    "picoftheday",
    "Follow",
    "me",
    "selfie",
    "summer",
    "art",
    "instadaily",
    "friends",
    "repost",
    "nature",
    "girl",
    "fun",
    "style",
    "smile",
    "food",
    "family",
    "travel",
    "fitness",
    "igers",
    "tagsforlikes",
    "follow4follow",
    "nofilter",
    "life",
    "beauty",
    "amazing",
    "instagram",
    "photography",
    "photo",
    "vscocam",
    "sun",]
        self.liczba = len(self.hashtags)
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(4)
        self.driver.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        time.sleep(3)
        self.rand = random.randint(1000,3000)
        self.rand = str(self.rand)
        self.driver.refresh()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(10," + self.rand + ")")
        print('current #', self.hashtags[self.hashtags_rand])
        time.sleep(3)
    
    ### ---> open_photo
    ### Function is responsible for open random picture on website.     
    def open_photo(self): 
        
        self.left = random.randint(1,3)
        self.left = str(self.left)
        self.downIndex = random.randint(2,5)
        self.downIndex = str(self.downIndex)
        self.photo = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div['+self.downIndex+']/div['+self.left+']/a')
        self.photo.click()
        time.sleep(2)
        
        
    ### ---> skip_photo
    ### Function is responsible for random skipp to next photo.    
    def skip_photo(self):
        time.sleep(2)
        self.skip_photo_button = self.driver.find_elements(By.CLASS_NAME,'_abl-')
        self.logic_skip_photo = random.randint(1,3)
        self.i = 0
        while self.i < self.logic_skip_photo:
            time.sleep(1.5)
            self.skip_photo_button = self.driver.find_elements(By.CLASS_NAME,'_abl-')
            time.sleep(1)
            self.skip_photo_button[1].click()
            self.i = self.i + 1
            print('skip {} photo, {}'.format(self.logic_skip_photo, self.i))    
            
     
    ### ---> like_photo_or_get_info
    ### Function is responsible for get user name and like photo.   
    def like_photo_or_get_info(self):
        
        time.sleep(0.5)
        self.like_button = self.driver.find_elements(By.CLASS_NAME,'xcdnw81')
        time.sleep(0.5)
        self.like_button[2].click()
        self.comm = self.driver.find_elements(By.CLASS_NAME,'xcdnw81')
        self.comm[13].click()
        self.comm = self.driver.find_elements(By.CLASS_NAME,'x1ja2u2z')
        self.rand = random.randint(1,5)
        self.x=0
        while self.x<self.rand:       
            self.comm[21].click()
            time.sleep(0.5)
            self.x=self.x+1
            
        print("Zdjęcie polaikowane.")    
        
        
    ### ---> next_photo
    ### Function is responsible for click to next photo.  
    def next_photo(self):
        time.sleep(2)
        self.next_photo_button = self.driver.find_element(By.CLASS_NAME,'_abl-')
        time.sleep(2)
        self.next_photo_button.click()
     
        
    ### ---> relax
    
    ### Function is responsible for pause.   
    def relax(self):
        
        self.relax_time = random.randint(42,82)
        print('InstaBotPy has stopped at this moment. The system will boot up in ', self.relax_time, ' seconds')
        time.sleep(self.relax_time)
        
    ### ---> change hash
    ### Function is responsible change hash.     
    def change_hash(self):
        
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(2)
        self.driver.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        print('# changed to # ' + self.hashtags[self.hashtags_rand])
        time.sleep(5)
    
    def random_like(self):
        
        self.amount = random.randint(10,20) # ammount like for # sesion.
        print('quantity like at this session - ', self.amount)
        
        
    ### ---> auto_like
    ### Function is responsible for auto like photo. 
    def auto_like(self):
        
        self.random_like()
        p_liked = 0
        while True:
            
          if p_liked == self.amount: # liczba przejsc petli:
              self.change_hash() 
              p_liked = 0
              self.relax()
              self.driver.refresh()
              time.sleep(7)
              try:
                  self.open_photo()
              except Exception:     
                  self.open_photo()
              time.sleep(4)
              self.skip_photo()
          else:
            time.sleep(5)
            try:
                self.like_photo_or_get_info()
            except Exception:     
                print("bład")      
            self.relax_after_like = random.randint(2,14)
            time.sleep(self.relax_after_like)
            self.next_photo()
            p_liked = p_liked + 1

bot = InstaPy()
bot.login()
bot.add_hashtags_and_search()     
bot.open_photo()   
bot.skip_photo()
bot.auto_like()
