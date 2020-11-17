import selenium

DRIVER_PATH = "/users/barre/OneDrive/prog/portfolio/project_vendor/website/driver/chromedriver.exe"

class EbayManager:
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)
    