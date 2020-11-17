from os import getcwd, path
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium

DRIVER_PATH = "/users/barre/OneDrive/prog/portfolio/project_vendor/browardreseller/static/driver/chromedriver.exe"

class DepopManager:
    # DRIVER_PATH = path.join (current_app.root_path, 'browardreseller/static/driver/chromedriver.exe')
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)
    login_url = "https://www.depop.com/login/"
    sell_url = "https://www.depop.com/products/create/"

    email = "browardreseller@gmail.com"
    pw = "Money$92"

    location = "pembroke pines, florida"

    def __init__(self):
        self.wd.implicitly_wait(5)

    def login(self):
        self.wd.get(self.login_url)
        email_box = self.wd.find_element(By.ID, "username")
        email_box.send_keys(self.email)
      
        pw_box = self.wd.find_element (By.ID, "password")
        pw_box.send_keys(self.pw)
        pw_box.send_keys(Keys.RETURN)
        sleep(3)

    
    def fill_form (self, model):
        self.wd.get(self.sell_url)
      
      #this description box uses hashes to create tags,
      #alter the details so that a hash is added.
 
        #this worked
        description_box = self.wd.find_element (By.ID, "description")
        for detail in model.details.split(" "):
            detail += "#"+detail
            description_box.send_keys(detail)



        #Menswear / Shoes
        try:                
            category_box = self.wd.find_element (By.XPATH, "//div[@class='listingSelect__value-container css-1hwfws3']")
            category_box.send_keys(model.c_type)
            category_box.send_keys(Keys.ENTER)

        except:
            pass

      # sub_category_box = self.wd.find_element (By.XPATH, "listingSelect__value-container listingSelect__value-container--has-value css-1hwfws3")
        
        try:                
            brand_div = self.wd.find_element (By.XPATH, "//div[@class='divCategoriesAndBrandsUIstyles__StyledBrandSelect-sc-1fzz1gd-1 fAwASm styles__Wrapper-sc-1xuh8ja-0 gZgYik']")
            brand_box = brand_div.find_element (By.XPATH, ".//div[@class='listingSelect__single-value css-1uccc91-singleValue']")
            brand_box.send_keys(model.brand)
            brand_box.send_keys(Keys.ENTER)
        except:
            pass

# listingSelect__value-container css-1hwfws3
        # listingSelect__single-value css-1uccc91-singleValue

      #only accepts string: "US SIZE_NUM if c_type is shoes"
        try:
            size_div = self.wd.find_element(By.XPATH, "//div[@data-testid='createProductSelect__createProductSizes__sizeRow0__size']")
            size_box = size_div.find_element(By.XPATH,".//div[@class='divCategoriesAndBrandsUIstyles__StyledBrandSelect-sc-1fzz1gd-1 fAwASm styles__Wrapper-sc-1xuh8ja-0 gZgYik']")
        except:
            pass


        # if model.c_type == "shoes":
        #     size_box.send_keys(model.size_asdict(key="country"),
        #                        model.size_asdict(key="size"))

        try:    
            location_box = self.wd.find_element(By.ID,"location_select")
            location_box.send_keys(self.location)
            location_box.send_keys(Keys.ENTER)
            selection = self.wd.find_element(By.ID,"option-63216822")
            selection.click()
        except:
            pass

    #     shipping_price_box = self.wd.find_element (By.ID,"national_shipping__manual")
    #     shipping_price_box.send_keys(model.shipping_price)

    #     price_box = self.wd.find_element(By.ID,"price")
    #     price_box.send_keys(Keys.ENTER)


    #     submit_btn = self.wd.find_element(By.CLASS_NAME,"Button__GenericButton-p20sh8-0 Button__ButtonPrimary-p20sh8-1 ibBTVs")
    #     submit_btn.click()
        sleep(10)



    def run(self, model):
        self.login()
        self.fill_form(model)


class Model:
    def __init__(self):
        self.details = "detail1 detail2 detail3"
        self.category = "shoes"
        self.c_type = "shoes"
        self.brand = "nike"
        self.location = "pembroke pines, florida"


if __name__=="__main__":
    m = Model ()
    whandler = DepopManager ()
    whandler.login()
    whandler.fill_form(m)    