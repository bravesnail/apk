# _*_coding: utf-8 _*_
import unittest
from time import sleep

from appium import webdriver
import uiautomator2
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'Pixel_2'
        desired_caps['appPackage'] = 'com.kwai.video'
        desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity'
        desired_caps['automationName'] = 'uiautomator2'
        # desired_caps['appWaitActivity'] = 'com.yxcorp.gifshow.login.SplashLoginActivity'
        desired_caps['resetKeyboard'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # createContactBtn = self.driver.tap([(200,1500)],100)
        # createContactBtn.click()
        #---login---#
        login_fb_btn = self.driver.find_element('xpath',"//android.widget.Button[contains(@text,'Facebook')]")
        login_fb_btn.click()
        # ---swich tab---#
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//android.widget.RadioButton[contains(@text,'Following')]")))
        if self.is_exist('ID','com.kwai.video:id/click_to_grant_storage_permission_button'):
            grant_but = self.driver.find_element_by_id('com.kwai.video:id/click_to_grant_storage_permission_button')
            grant_but.click()
            sleep(1)
        if self.is_exist('ID','com.android.packageinstaller:id/permission_allow_button'):
            allow_btn = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
            allow_btn.click()
            sleep(1)
            allow_btn = self.driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        # print allow_btn
            allow_btn.click()
            sleep(1)
        sleep(5)
        follow_tab = self.driver.find_element('xpath',"//android.widget.RadioButton[contains(@text,'Following')]")
        follow_tab.click()

        sleep(1)
        self.driver.save_screenshot('screenshot/swich_follow.png')
        if self.is_exist('ID','com.kwai.video:id/tv_allow'):
            contact_allow = self.driver.find_element_by_id('com.kwai.video:id/tv_allow')
            contact_allow.click()
            sleep(1)
            ALLOW_btn = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
            ALLOW_btn.click()
            sleep(1)
        self.driver.save_screenshot('screenshot/contact_allow.png')
        # ---click like---#
        trend_tab = self.driver.find_element('xpath', "//android.widget.RadioButton[contains(@text,'Trending')]")
        trend_tab.click()
        photos = self.driver.find_elements_by_android_uiautomator('new UiSelector().description("Posts")')
        print(len(photos))
        for photo in photos:
            photo.click()
            self.like_it()
            self.driver.back()
        self.driver.save_screenshot('screenshot/like_it.png')
        # ---koin---#
        if self.is_exist('ID','com.kwai.video:id/avatar'):
            side_bar = self.driver.find_element_by_id('com.kwai.video:id/avatar')
            side_bar.click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,'com.kwai.video:id/item_name')))
            wallet = self.driver.find_element_by_id('com.kwai.video:id/item_name')
            wallet.click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,'com.kwai.video:id/withdraw_rl')))
            withdraw = self.driver.find_element_by_id('com.kwai.video:id/withdraw_rl')
            withdraw.click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[contains(@text,'Withdraw to PayPal')]")))
            withdraw_paypal = self.driver.find_element(By.XPATH,"//android.view.View[contains(@text,'Withdraw to PayPal')]")
            withdraw_paypal.click()
            sleep(1)
            self.driver.save_screenshot('screenshot/withdraw_paypal.png')
            self.driver.back()
            self.driver.back()
        # ---profile share---#
        # if self.is_exist('ID','com.kwai.video:id/avatar'):
        #     side_bar = self.driver.find_element_by_id('com.kwai.video:id/avatar')
        #     side_bar.click()
        #     WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID,"com.kwai.video:id/tab_avatar")))
        #     profile_btn = self.driver.find_element_by_id('com.kwai.video:id/tab_avatar')
        #     profile_btn.click()
        #     sleep(1)
        #     if self.is_exist('XPATH',"//android.widget.Button[contains(@text,'ALLOW')]"):
        #         allow_btn = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'ALLOW')]")
        #         allow_btn.click()
        #     WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID,"com.kwai.video:id/share_profile_btn")))
        #     share_btn = self.driver.find_element_by_id('com.kwai.video:id/share_profile_btn')
        #     share_btn.click()
        #     WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[contains(@text,'Facebook')]")))
        #     share_to_fb = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'Facebook')]")
        #     share_to_fb.click()
        #     WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[contains(@text,'POST')]")))
        #     input_text = self.driver.find_element(By.XPATH,"//android.widget.EditText[contains(@text,'Write something…')]")
        #     input_text.send_keys(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     sleep(1)
        #     post_btn = self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'POST')]")
        #     post_btn.click()
        #     self.driver.save_screenshot('screenshot/share_to_fb.png')
        #     sleep(5)
        #     self.driver.back()

        # ---record---#
        torecord_btn = self.driver.find_element_by_id('com.kwai.video:id/right_btn')
        torecord_btn.click()
        sleep(2)
        while self.is_exist('XPATH', "//android.widget.Button[contains(@text,'ALLOW')]"):
            allow_btn = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'ALLOW')]")
            allow_btn.click()
            sleep(1)
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID,'com.kwai.video:id/camera_magic_emoji_btn')))
        magic_btn = self.driver.find_element_by_id('com.kwai.video:id/camera_magic_emoji_btn')
        magic_btn.click()
        # WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID,'com.kwai.video:id/forbidden_magic_emoji')))
        if not self.is_exist('ID','com.kwai.video:id/forbidden_magic_emoji'):
            magic_btn.click()
        magic_list = self.driver.find_elements_by_id('com.kwai.video:id/magic_emoji_cover')
        self.assertGreater(len(magic_list),5)
        magic_0 = magic_list[0]
        magic_0.click()
        sleep(10)
        self.assertTrue(magic_0.is_selected())
        self.driver.back()
        record_btn = self.driver.find_element_by_id('com.kwai.video:id/record_tap')
        record_btn.click()
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID,'com.kwai.video:id/right_btn')))
        conform_btn = self.driver.find_element_by_id('com.kwai.video:id/right_btn')
        conform_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'com.kwai.video:id/editor')))
        input_text = self.driver.find_element_by_id('com.kwai.video:id/editor')
        input_text.send_keys(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        share_cancle = self.driver.find_elements_by_class_name('android.widget.CheckBox')[0]
        share_cancle.click()
        self.driver.save_screenshot('screenshot/ready_to_post.png')
        post_btn = self.driver.find_element_by_id('com.kwai.video:id/post')
        post_btn.click()
        if self.is_exist('ID','com.kwai.video:id/positive_btn'):
            positivi_btn = self.driver.find_element_by_id('com.kwai.video:id/positive_btn')
            positivi_btn.click()
            sleep(1)
        if self.is_exist('XPATH', "//android.widget.Button[contains(@text,'ALLOW')]"):
            allow_btn = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'ALLOW')]")
            allow_btn.click()
            sleep(1)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.RadioButton[contains(@text,'Following')]")))
        self.driver.save_screenshot('screenshot/post_success.png')







        # name_input = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'姓名')]")
        # name_input = self.driver.find_element('xpath',"//android.widget.EditText[contains(@text,'姓名')]")
        # name_input.click()
        # name_input.send_keys('appium test')
        # phonenum_input = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'手机')]")
        # phonenum_input.click()
        # phonenum_input.send_keys('12345678')
        # save_btn = self.driver.find_element_by_id('com.samsung.android.contacts:id/menu_done')
        # save_btn.click()
        # sleep(1)
        #
        # self.driver.save_screenshot("saved.png")
        # getnum = self.driver.find_element_by_id('com.samsung.android.contacts:id/text').text
        # self.assertEqual(getnum,'12345 678')
        # more_btn = self.driver.find_element_by_accessibility_id('更多选项')
        # more_btn.click()
        # del_btn = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'删除')]")
        # del_btn.click()
        # sleep(1)
        # self.driver.save_screenshot('del.png')
        # del2_btn = self.driver.find_element_by_id('android:id/button1')
        # del2_btn.click()
        # self.driver.save_screenshot('del_success.png')
    def is_exist(self,type,content):
        # print(id)
        try:
            if type=='ID':
                    self.driver.find_element_by_id(content)
                    return True
            elif type=='XPATH':
                    self.driver.find_element_by_xpath(content)
                    return True
        except NoSuchElementException:
            return False
    def like_it(self):
        like_btn = self.driver.find_element_by_id('com.kwai.video:id/like_button')
        like_btn.click()
        sleep(1)
        self.assertTrue(like_btn.is_selected())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)


