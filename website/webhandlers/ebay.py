import contextlib
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from os import getcwd
import selenium



IMGS_PATH = getcwd()+""
# DRIVER_PATH = "/users/barre/OneDrive/prog/portfolio/project_vendor/browardreseller/driver/chromedriver.exe"

DRIVER_PATH = "/users/barre/OneDrive/prog/portfolio/project_vendor/browardreseller/static/driver/chromedriver.exe"


class EbayManager:
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)
    login_url = "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F"
    sell_url = "https://www.ebay.com/sl/sell?sr=wnstart"

    email = "barreraalexander93@gmail.com"
    pw = "Barr1993"


    def __init__(self):
        self.wd.implicitly_wait(5)
        # self.waiting = ui.WebDriverWait (self.wd, 1000)

    def login (self):
        self.wd.get(self.login_url)
        sleep(90)

        # email_box = self.wd.find_element_by_id ("userid")
        # email_box.send_keys(self.email)
        # email_box.send_keys(Keys.RETURN)

        # pw_box = self.wd.find_element_by_id ("pass")
        # pw_box.send_keys(self.pw)
        # pw_box.send_keys(Keys.RETURN)
        
        # self.waiting.until (self.wd.find_element(By.ID, "gh-ug"))
        # self.waiting.until(lambda x: x.)


    def sell_item (self, model):
        self.wd.get (self.sell_url)
        category = model.category

        category_box = self.wd.find_element_by_id ("smac_complete")
        category_box.send_keys (category)
        category.send_keys (Keys.RETURN)
        category.send_keys (Keys.RETURN)

        newlisting_btn = self.wd.find_element_by_class_name("callToAction__btn")
        newlisting_btn.click()

        if model.condition == "new":
            radio_select = self.wd.find_element_by_id("Conditoin0")

        elif model.condition == "used":
            radio_select = self.wd.find_element_by_id("Condition1")

        radio_select.click()
        self.fill_sell_form(self, model)

    def fill_sell_form (self, model):
        title_box = self.wd.find_element_by_id("wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-TITLE__-titleField__-textbox")

        #model details will be a dictionary
        for detail in model.details:
            if detail != None:
                title_box.send_keys(detail)
    
        # form_inputs = self.wd.find_elements_by_class_name("grid__cell")
        form_inputs = self.wd.find_elements(By.CLASS_NAME, "grid__cell")

        for i, elem in enumerate(form_inputs):
            elem_xpath = ".//span[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-RECOMMENDED_GROUP__-RECOMMENDED_ATTRIBUTE_GRID__-topRecommendedAttrList.{i}__-valueSelect-w0']"
            elem_span = elem.find_element (By.XPATH, elem_xpath)
            key = elem_span.text
            key = key.lower()

            try:
                #keep in mind that the input tag isn't generated (or is hidden) until the box is clicked
                detail = model.details[key]
                input_xpath = ".//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-RECOMMENDED_GROUP__-RECOMMENDED_ATTRIBUTE_GRID__-topRecommendedAttrList.{i}__-valueSelect-searchBox-input'"
                input_box = elem.find_element (By.XPATH, input_xpath)
                input_box.send_keys (detail)
                input_box.send_keys (Keys.RETURN)
            except:
                pass

        ##now it's time to add photos
        #click the upload button
        button_xpath = "//button[@class='jsPhotoUploaderButton needsclick']"
        for img_path in model.img_paths:
            upload_pic_btn = self.wd.find_element(By.XPATH, button_xpath)
            upload_pic_btn.send_keys(img_path)

        # upload_pic_btn.click()

        ##fill in pricing stuff
        price_box_name = "startPrice"
        price_box = self.wd.find_element(By.NAME, price_box_name)
        price_box.send_keys(model.selling_price)


        
        easy_pricing_box = self.wd.find_element(By.NAME, "easyPriceSelection")
        easy_pricing_box.click()

        bin_box = self.wd.find_element(By.NAME, "binPriceSelection")
        bin_box.click()

        bin_price_box = self.wd.find_element(By.NAME, "price")
        bin_price_box.send_keys(model.orig_value/2)      


    def run (self, model):
        self.login()
        self.sell_item(model)


class Model:
    def __init__(self):
        self.details = "detail1 detail2 detail3"
        self.category = "shoes"

def main():
    whandler = EbayManager ()
    whandler.login()
    whandler.sell_item(model=None)

if __name__=="__main__":
    main()
    # C:\Users\barre\OneDrive\prog\portfolio\project_vendor\browardreseller\static\images\item_images\randomtokenhex
