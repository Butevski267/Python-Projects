from selenium import webdriver
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SPEEDTEST_URL = "https://www.speedtest.net/"

TWITTER_EMAIL = "Your Twitter Email"
TWITTER_PASS = "Your Twitter Password"
INTERNET_PROVIDER = 'Your Internet provider name'

PROMISED_DOWN = 20
PROMISED_UP = 15



class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        #driver.get(url=URL)
        self.down = 0
        self.up = 0
        self.letter = f"Hey {INTERNET_PROVIDER}, why is my download speed: {self.down}Mbps and my upload speed: {self.up}Mbps, when I pay for a 150Mbps download and 1Mpbs upload speed? "

    def get_internet_speed(self,url):
        self.driver.get(url=url)
        button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        button.click()
        time.sleep(45)

        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"Download: {self.down}")
        print(f"Upload: {self.up}")

    def tweet_at_provider(self,PROMISED_UP,PROMISED_DOWN):
        if float(self.up) < PROMISED_UP or float(self.down) < PROMISED_DOWN:
            self.driver.get(url = 'https://twitter.com/')
            time.sleep(5)
            sign_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
            sign_in_button.click()
            time.sleep(3)
            input_field = self.driver.find_element_by_name('text')
            input_field.send_keys(TWITTER_EMAIL)
            time.sleep(2)
            next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span')
            next_button.click()
            time.sleep(3)
            input_field = self.driver.find_element_by_name('password')
            input_field.send_keys(TWITTER_PASS)
            time.sleep(2)
            log_in_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
            log_in_button.click()
            time.sleep(5)
            status_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            status_field.send_keys(self.letter)
            time.sleep(3)
            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet.click()
            time.sleep(10)
            driver.quit()
        else:
            driver.quit()

twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed(SPEEDTEST_URL)
twitter_bot.tweet_at_provider(PROMISED_UP, PROMISED_DOWN)

