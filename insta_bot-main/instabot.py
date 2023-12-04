import os
import time
import pyodbc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import random


class InstaPy:
    query = 'SELECT Name, Follows, Comments, Likes, Runtime FROM instabots;'
    connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:eatme-server.database.windows.net,1433;Database=instabotDB;Uid=eatme-admin;Pwd=KRA@ie#13;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        instabot = {
            'Name': row[0],
            'Follows': row[1],
            'Comments': row[2],
            'Likes': row[3],
            'Runtime': row[4]
        }
    update = "UPDATE instabots SET Follows=?, Comments=?, Likes=?, Runtime=?  WHERE Name=?"
    cursor.execute("UPDATE instabots SET Status=? WHERE Name=?",True,"Aries")
    conn.commit()
    conn.close()

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

        # Funkcja odpowiedzialna za otworzenie instagrama i zalogowanie.

    def login(self):
        os.system('cls')
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.login = "ChicStreetFashion2" ### <--- Tu wprowadź login
        self.wantlike = "1" ### <---Czy bot ma laikować posty? Wprowadź 1 jeśli tak lub 0 jeśli nie
        self.wantcomment ="1" ### <---Czy bot ma komentowac posty? Wprowadź 1 jeśli tak lub 0 jeśli nie
        self.wantfollow = "1" ### <---Czy bot ma zostawić follow? Wprowadź 1 jeśli tak lub 0 jeśli nie
        self.password = "Hasełko20!"  ### <--- Tu wprowadź hasło
        time.sleep(5)
        # ---> Zaakceptowanie Cookies.
        self.acceptbutton = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        time.sleep(2)
        try:
            self.acceptbutton.click()
        except:
            self.acceptbutton = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
            self.acceptbutton.click()


        time.sleep(2)
        # Wypełnienie i wysłanie formularza logowania.
        self.emailForm = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        time.sleep(1)
        self.passwordForm = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        time.sleep(1)
        self.loginButton = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        time.sleep(1)
        self.loginButton.click()
        time.sleep(15)
        self.instabot['Runtime'] += 27

    ### Funkcja odpowiedzialna za wybór hashtagu i wyszukanie go na instagramie.
    def add_hashtags_and_search(self):

        self.hashtags = [
            "love", "instagood", "instagram", "fashion", "photooftheday",
    "art", "photography", "beautiful", "nature", "picoftheday",
    "travel", "happy", "follow", "cute", "style",
    "instadaily", "tbt", "repost", "summer", "beauty",
    "followme", "fitness", "like4like", "food", "instalike",
    "explore", "photo", "me", "viral", "music",
    "life", "friends", "family", "fun", "girl",
    "selfie", "makeup", "likeforlikes", "dog", "smile",
    "explorepage", "model", "design", "motivation", "handmade",
    "lifestyle", "likeforlike", "sunset", "artist", "dogsofinstagram",
    "ootd", "foodporn", "beach", "followforfollowback", "drawing",
    "amazing", "cat", "instamood"]
        self.liczba = len(self.hashtags)
        self.hashtags_rand = random.randint(0, self.liczba - 1)
        time.sleep(4)
        self.driver.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/')
        time.sleep(3)
        self.rand = random.randint(1000, 3000)
        self.rand = str(self.rand)
        self.driver.refresh()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(10," + self.rand + ")")
        print('Wybrany #:', self.hashtags[self.hashtags_rand])
        time.sleep(3)
        self.instabot['Runtime'] += 15

    ###Funkcja odpowiedzialna za otwracie losowego zdjęcia na stronie.
    def open_photo(self):

        self.downIndex = random.randint(1,2)
        self.downIndex = str(self.downIndex)
        self.leftIndex = random.randint(2, 3)
        self.leftIndex = str(self.leftIndex)
        try:
            self.photo = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[' + self.downIndex + ']/div[' + self.leftIndex + ']/a')
        except Exception:
            self.driver.refresh()
        self.photo.click()
        time.sleep(2)
        self.instabot['Runtime'] += 2

    ###Funkcja odpowiedzialna za losowe pominięcie zdjęć.   
    def skip_photo(self):
        time.sleep(2)
        self.skip_photo_button = self.driver.find_elements(By.CLASS_NAME, '_abl-')
        self.logic_skip_photo = random.randint(1, 3)
        self.i = 0
        while self.i < self.logic_skip_photo:
            time.sleep(1.5)
            self.skip_photo_button = self.driver.find_elements(By.CLASS_NAME, '_abl-')
            time.sleep(1)
            self.skip_photo_button[1].click()
            self.i = self.i + 1
        if self.logic_skip_photo == 1:
            print("Pominięto: " + str(self.logic_skip_photo) + " zdjęcie")
        else:
            print("Pominięto: " + str(self.logic_skip_photo) + " zdjęcia")
        self.instabot['Runtime'] += 4

    ### Funkcja odpowiedzialnie za zostawienie like i napisania losowego komentarza(ok 10% szans).
    def like_photo_and_comment(self):
        self.mess=""
        time.sleep(0.5)
        if self.wantlike=="1":
            self.like_button = self.driver.find_elements(By.CLASS_NAME, 'xcdnw81')
            time.sleep(0.5)
            self.like_button[2].click()
            self.instabot['Likes'] += 1
            self.mess=self.mess+"Zdjęcie polaikowane"
        self.commentif = random.randint(1, 100)
        self.followif = random.randint(1, 100)
        self.rand = random.randint(1, 5)
        self.instabot['Runtime'] += 1
        self.x = 0
        if self.commentif > 80 and self.followif > 80:
            try:
                if self.wantcomment == "1":
                    self.left_comment()
                    self.mess=self.mess+" komentarz"
                    self.instabot['Comments'] += 1
                try:
                    if self.wantfollow == "1":
                      self.left_follow()
                      self.mess = self.mess + ", follow"
                      self.instabot['Follows'] += 1
                except:

                    self.instabot['Comments'] += 1
                    self.mess=self.mess+" komentarz"
            except:
                try:
                    if self.wantfollow == "1":
                        self.left_follow()
                        self.instabot['Follows'] += 1
                        self.mess = self.mess + ", follow"
                except:
                    self.mess=self.mess
                self.mess=self.mess+", follow"
            print(self.mess)
        elif self.commentif > 80:
            try:
                if self.wantcomment == "1":
                    self.left_comment()
                    self.instabot['Comments'] += 1
                    self.mess=self.mess+" komentarz"
            except:
                self.mess=self.mess
            print(self.mess)
        elif self.followif > 80:
            try:
                if self.wantfollow == "1":
                    self.left_follow()
                    self.instabot['Follows'] += 1
                    self.mess=self.mess+" follow"
            except:
                 self.mess=self.mess
            print(self.mess)
        else:
            print(self.mess)

    ###Funkcja odpowiedzialna za zostawienie komentarza.      
    def left_comment(self):
        self.comm = self.driver.find_element(By.XPATH,
                                             '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[1]/div')
        self.comm.click()
        time.sleep(2)
        self.instabot['Runtime'] += 2
        while self.x < self.rand:
            self.emote = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[6]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[7]/div')
            self.emote.click()
            time.sleep(0.5)
            self.x = self.x + 1
            self.instabot['Runtime'] += 1
        self.sent = self.driver.find_element(By.XPATH,
                                             '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div')
        self.sent.click()

    ###Funkcja odpowiedzialna za zostawienie followa.
    def left_follow(self):
        self.follow = self.driver.find_element(By.XPATH,
                                               '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button')
        self.follow.click()
        time.sleep(2)
        self.instabot['Runtime'] += 2

    ###Funkcja odpowiedzialna za kliknięcie "Dalej".
    def next_photo(self):
        time.sleep(2)
        self.next_photo_button = self.driver.find_element(By.XPATH,
                                                          '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
        time.sleep(2)
        self.next_photo_button.click()
        self.instabot['Runtime'] += 4

    ###Funkcja odpowiedzialna za przerwę w działaniu bota. 
    def relax(self):
        self.relax_time = random.randint(600, 900)
        self.y = 0
        self.count = self.relax_time
        self.instabot['Runtime'] += self.count
        print("")
        for self.y in range(self.relax_time):
            self.relax_time = self.relax_time - 1
            print('InstaBot zrobił sobie chwilę przerwy, wróci do pracy za: ' + str(self.relax_time) + 's', end="\r")
            time.sleep(1)
        print("InstaBot zrobił sobie " + str(self.count) + "s przerwy,ale wrócił już do pracy :)", end="\r")
        print("")

    ### Funkcja odpowiedzialna za zmiane hashtagu.
    def change_hash(self):

        self.hashtags_rand = random.randint(0, self.liczba - 1)
        time.sleep(2)
        self.driver.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/')
        print('# zmieniony na: ' + self.hashtags[self.hashtags_rand])
        time.sleep(5)
        self.instabot['Runtime'] += 7

    def random_like(self):

        self.amount = random.randint(18, 22)  # Liczba polubień na jedną sesję.
        print('Ilość like na sesje: ', self.amount)

    ###Funkcja odpowiedzialna za polubienie zdjęć.
    def auto_like(self):

        self.random_like()
        p_liked = 0
        while True:
            if p_liked >= self.amount:  # liczba przejść petli:
                self.change_hash()
                p_liked = 0
                self.relax()
                self.driver.refresh()
                time.sleep(8)
                self.instabot['Runtime'] += 8
                try:
                    self.open_photo()
                except Exception:
                    self.open_photo()
                time.sleep(4)
                self.instabot['Runtime'] += 4
                self.skip_photo()
            else:
                time.sleep(5)
                self.instabot['Runtime'] += 5
                try:
                    self.like_photo_and_comment()
                except Exception:
                    print("Coś poszło nie tak")
                    self.next_photo()
                self.relax_after_like = random.randint(4,10)
                time.sleep(self.relax_after_like)
                self.instabot['Runtime'] += self.relax_after_like
                try:
                    self.next_photo()
                except Exception:
                    print("Nie można przejść do następnego zdjęcia")
                    p_liked=self.amount
                p_liked = p_liked + 1
                try:
                    self.conn = pyodbc.connect(self.connectionString)
                    self.cursor = self.conn.cursor()

                    self.cursor.execute(self.update, self.instabot['Follows'], self.instabot['Comments'],
                                    self.instabot['Likes'], self.instabot['Runtime'], self.instabot['Name'])
                    self.conn.commit()
                    self.cursor.close()
                    self.conn.close()
                except:
                    print("Połączenie z bazą nie udało się")
                print(self.instabot)

try:
    bot = InstaPy()
    bot.login()
    bot.add_hashtags_and_search()
    bot.open_photo()
    bot.skip_photo()
    bot.auto_like()
except:
    connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:eatme-server.database.windows.net,1433;Database=instabotDB;Uid=eatme-admin;Pwd=KRA@ie#13;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("UPDATE instabots SET Status=? WHERE Name=?", False, "Aries")
    conn.commit()
    conn.close()